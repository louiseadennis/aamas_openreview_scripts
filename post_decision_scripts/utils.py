import openreview
import numpy as np
import country_converter as cc

# generate and store the set of all submissions with all needed information
# from OpenReview
class SubmissionSet:
    
    def __init__(self,client=None,venue_id=None,accepted_only=False,decision_set=["full"]):

        self.submissions = {}

        if not client or not venue_id:
            return
        
        venue_group = client.get_group(venue_id)
        self.addSubmissions(client,venue_group,venue_id,accepted_only,decision_set)

    def addSubmissions(self,client,venue_group,venue_id,accepted_only=False,decision_set=["full"]):
        venue_group_settings = venue_group.content
        
        
        
        submission_name = venue_group_settings['submission_name']['value']
        submission_invitation = venue_group_settings['submission_id']['value']
        decision_invitation_name = venue_group_settings['decision_name']['value']
        #review_name = venue_group_settings['review_name']['value']

        submissions = client.get_all_notes(
            invitation=submission_invitation,
            details='replies'
        )

        counter = 1
        for s in submissions:
        
            add_this_one = False
                #     if (not f'{venue_id}/-/Desk_Rejected_Submission' in s.invitations):
        # print(note)
                 #        if (not f'{venue_id}/-/Withdrawn_Submission' in s.invitations):
            decision = ""
                
            for reply in s.details['replies']:
                for invitation in reply['invitations']:
                    if invitation.endswith("Decision"):
                        decision = reply['content']['decision']['value']
                            
                        if ((decision == "Accept (Full)" and "full" in decision_set) or (decision == "Accept (Extended Abstract)" and "ea" in decision_set)):
                                add_this_one = True
            if not accepted_only:
                add_this_one = True


            # add basic submission information
            if add_this_one:
                self.addSubmission(s)

                # add reviews
                #self.addReviews(s,venue_id,submission_name,review_name)

                # add authors
                author_list = s.content['authors']['value']
                author_ids_list = s.content['authorids']['value']
                                # print(author_list)
                                # print(author_ids_list)
                author_profiles = openreview.tools.get_profiles(client, author_ids_list)
                author_list = []
                author_id_to_name = {}
                for profile in author_profiles:
                    found_name = False
                                    # print(profile)
                    username = profile.id
                    if (username not in author_ids_list):
                        for name in profile.content['names']:
                            if name['username'] in author_ids_list:
                                username = name['username']
                    for name in profile.content['names']:
                        if ('preferred' in name.keys() and name['preferred']):
                            print("adding1 " + username)
                            author_id_to_name[username] = name['fullname']
                            found_name = True
                            break
                    if (not found_name):
                        print("adding " + username)
                        author_id_to_name[username] = profile.content['names'][0]['fullname']

                for id in author_ids_list:
                    author_list.append(author_id_to_name[id])
                    
                print(author_list)
                self.submissions[s.number].addAuthors(client,author_list,author_ids_list)

                # add decision
                for reply in s.details['replies']:
                    if any(invitation.endswith(f'/-/{decision_invitation_name}') for invitation in reply['invitations']):

                        decision = reply['content']['decision']['value']
                        self.submissions[s.number].addDecision(decision)

                # keep track of how many submissions have been loaded
                # it'll say silly things like "1th" submission,
                # but not worth the trouble dealing with that...
                print("added "+str(counter)+"th "+"submission ("+str(s.number)+")")
                counter = counter + 1
        print("Total submissions " + str(counter - 1))
                    
    def addReviews(self,submission,venue_id,submission_name,review_name):

        for reply in submission.details['replies']:
            if f'{venue_id}/{submission_name}{submission.number}/-/{review_name}' in reply['invitations']:
                review_text = reply['content']['review']['value']
                technical_quality = reply['content']['overall_rating']['value']
                significance = reply['content']['significance']['value']
                presentation = reply['content']['presentation_quality']['value']
                overall_rating = reply['content']['overall_rating']['value']
                confidence = reply['content']['confidence']['value']

                review = Review(review_text,technical_quality,significance,presentation,overall_rating,confidence)
                
                self.submissions[submission.number].addReview(review)
        

    def addSubmission(self,submission):

        paper_id = submission.number
        title = submission.content['title']['value']
        track = submission.content['area']['value']
        
        s = Submission(paper_id,title,track)
        
        self.submissions.update({paper_id: s})

    # output a list of submissions in a desired format (csv or xml)
    # @decision_filter subselects accepted full papers, extended abstracts, or rejected; specified in short format (full, ea, reject)
    # @track_filter subselects a track, specified in short format (GTEP, LEARN, etc)
    # @score_filter subselects those with average score at least score_filter
    def printPapers(self,output_format,
                         year,
                         submission_subset=None,
                         author_print_format=None,
                         decision_filter=None,track_filter=None,score_filter=None,submission_date=None,decision_date=None):

        if not author_print_format or not (author_print_format in ["short", "long"]):
            author_print_format = "short"

        if output_format == "xml":
            print("<erights_record>")
            print("  <parent_data>")

            if decision_filter == ["full"]:
                print("  <proceeding>AAMAS-"+year+" Full Papers (Main Track)</proceeding>")
            elif decision_filter == ["ea"]:
                print("  <proceeding>AAMAS-"+year+" Extended Abstracts (Main Track)</proceeding>")
                    
            print("  </parent_data>")
            
        for s in self.submissions.values():
            if self.checkFilter(s,submission_subset,decision_filter,track_filter,score_filter):
                # print this submission
                if output_format == "csv":
                    print(s.getCSV(author_print_format))

                if output_format == "xml":                    
                    s.printXML(submission_date, decision_date)

        if output_format == "xml":
            print("</erights_record>")
        
        return 0

    # count the number of submissions, full, ea, reject
    def printCounts(self,track_filter=None):
        full = 0
        ea = 0
        reject = 0
        
        for s in self.submissions.values():

            if self.checkFilter(s,None,"full",track_filter,None):
                full = full + 1

            if self.checkFilter(s,None,"ea",track_filter,None):
                ea = ea + 1

            if self.checkFilter(s,None,"reject",track_filter,None):
                reject = reject + 1

        total = full + ea + reject

        full_pr = int(round(100*full / total,0))
        accept_pr = int(round(100*(full+ea)/total,0))
                
        print("total: "+str(total)+",","full: "+str(full)+" ("+str(full_pr)+"%)"+",","full+ea: "+str(full+ea)+" ("+str(accept_pr)+"%)")


    def printReviewLength(self,track_filter=None):
        review_length = 0
        num_submissions = 0
        num_reviews = 0
        
        for s in self.submissions.values():

            if self.checkFilter(s,None,None,track_filter,None):
                num_submissions = num_submissions + 1
                review_length = review_length + s.totalReviewLength()
                num_reviews = num_reviews + s.getNumReviews()


        average_review_length = int(round(review_length / num_reviews,0))
                
        print("total number of reviews: "+str(num_reviews)+",","average length: "+str(average_review_length))


    def printAverageScores(self,track_filter=None):
        total = 0
        total_scores = 0

        for s in self.submissions.values():
            
            if self.checkFilter(s,None,None,track_filter,None):
                ave_score = s.getAverageScore()
                if (ave_score > 0):
                    total = total + 1
                    total_scores = total_scores + ave_score

               
        average_score = total_scores / total

        print("average score: ",average_score)
        
    # check if a submission (object) passes the specified filter
    def checkFilter(self,submission,
                         submission_subset=None,
                         decision_filter=None,track_filter=None,score_filter=None):
        
        if submission_subset and not submission.getID() in submission_subset:
            return False
        
        if decision_filter and not submission.decisionIsIn(decision_filter):
            return False

        if track_filter and not submission.isInTrackSet(track_filter):
            return False

        if score_filter and submission.getAverageScore() < score_filter:
            return False
        
        return True

class Submission:

    track_list = [  "Learning and Adaptation (LEARN)",
                    "Generative and Agentic AI (GAAI)",
                    "Game Theory and Economic Paradigms (GTEP)",
                    "Coordination, Organisations, Institutions, Norms and Ethics (COINE)",
                    "Search, Optimization, Planning, and Scheduling (SOPS)",
                    "Representation and Reasoning (RR)",
                    "Engineering and Analysis of Multiagent Systems (EMAS)",
                    "Modelling and Simluation of Societies (SIM)",
                    "Human-Agent Interaction (HAI)",
                    "Robotics and Control (ROBOT)",
                    "Innovative Applications (IA)"]
        
    track_list_short = ["LEARN", "GAAI", "GTEP", "COINE", "SOPS", "RR", "EMAS", "SIM", "HAI", "ROBOT", "IA"]

    decision_space = ["Accept (Full)", "Accept (Extended Abstract)", "Reject"]
    decision_space_short = ["full", "ea", "reject"]
    
    def __init__(self,paper_id,title,track_long):
        self.id = paper_id
        self.title = title
        
        # submission track (full track description)
        self.track_long = track_long

        # submission track (short track name)
        self.track_short = self.getTrackShort(track_long)

        self.decision = ""
        self.decision_short = ""

        # a list of all authors and their information
        self.authors = []
        
        # a list of all reviews (classes)
        self.reviews = []

    def addDecision(self,decision):
        # decision
        self.decision = decision
        self.decision_short = self.getDecisionShort(decision)

        
    def addReview(self,review):
        self.reviews.append(review)

    def addAuthors(self,client,author_names,author_ids):
        seq_no = 1
        for i in range(len(author_ids)):
            author_name = author_names[i]
            author_id = author_ids[i]
            author_profile = openreview.tools.get_profiles(client, [author_id])[0]
            author = Author(author_name,author_profile,seq_no)
            self.authors.append(author)

    def getID(self):
        return self.id
        
    # get the short track name from the long track name
    def getTrackShort(self,track_long):
        i = self.track_list.index(track_long)
        return self.track_list_short[i]

    # get the long track name from the short track name
    def getTrackLong(self,track_short):
        i = self.track_list_short.index(track_short)
        return self.track_list[i]

    def isInTrackShort(self,track_short):
        return self.track_short == track_short

    def isInTrackLong(self,track_long):
        return self.track_long == track_long

    # checks if the submission is in the specified track
    # tracks are specified in short form (LEARN, GTEP, etc)
    def isInTrack(self,track):
        return self.isInTrackShort(track)

    def isInTrackSet(self,track_set):
        return self.track_short in track_set
    
    # ditto for decision strings
    def getDecisionShort(self,decision_long):
        i = self.decision_space.index(decision_long)
        return self.decision_space_short[i]
    
    def getDecisionLong(self,decision_short):
        i = self.decision_space_short.index(decision_short)
        return self.decision_space[i]

    # returns decision in short format (full, ea, reject)
    def decisionIs(self,decision):
        return self.decision_short == decision

    def decisionIsIn(self,decision_set):
        if not self.decision_short:
            return False
        
        return self.decision_short in decision_set

    def getAverageScore(self):
        average_score = 0.0
        num_reviews = len(self.reviews)

        if (num_reviews == 0):
            return 0

        for review in self.reviews:
            average_score = average_score + review.getScore()

        return average_score / num_reviews

    def totalReviewLength(self):
        review_length = 0.0

        for review in self.reviews:
            review_length = review_length + review.getTextLength()

        return review_length

    def getNumReviews(self):
        return len(self.reviews)
    
    def printXML(self,submission_date, decision_date):

        if not submission_date or not decision_date:
            print("Usage: Submission.printXML(submission_date, decision_date)")
            return
        
        print("  <paper>")

        if self.decision_short == "full":
            print("    <paper_type>Full Paper (Main Track)</paper_type>")
            
        elif self.decision_short == "ea":
            print("    <paper_type>Extended Abstract (Main Track)</paper_type>")

        print("    <art_submission_date>"+submission_date+"</art_submission_date>")
        print("    <art_approval_date>"+decision_date+"</art_approval_date>")

        print("    <paper_title>"+str(self.title)+"</paper_title>")

        if self.decision_short == "full":
            print("    <event_tracking_number>fp"+str(self.id)+"</event_tracking_number>")
            
        elif self.decision_short == "ea":
            print("    <event_tracking_number>ea"+str(self.id)+"</event_tracking_number>")


        print("    <authors>")
        author_no = 1        
        for author in self.authors:
            author.printXML(author_no, "Y")
            author_no = author_no + 1
            
        print("    </authors>")
        print("  </paper>")
        
        return 0

    def getCSV(self,author_print_format):
        
        csv_str = str(self.id)+"\t"+self.title+"\t"

        num_authors = len(self.authors)
        for i in range(num_authors):
            author = self.authors[i]
            csv_str = csv_str + author.getCSV(author_print_format)
            if i < num_authors - 1:
                csv_str = csv_str + ", "
                                
        return csv_str

class Author:

    def __init__(self,full_name,profile,seq_no):
        self.full_name = full_name
        self.profile = profile
        self.seq_no = seq_no
        
        self.first_name = ""
        self.middle_name = ""
        self.last_name = ""

        self.parseName(full_name)
        
        self.institution = ""        
        self.country = ""
        self.country_code = ""
        self.city = ""
        self.state = ""
        self.email = ""

        self.parseAffiliation(profile)

    def parseName(self,name):
        name_array = name.split(' ')
        num_name_parts = len(name_array)
                    
        if (num_name_parts > 0):
            self.first_name = name_array[0]
                    
        for j in range(1,num_name_parts-1):
            self.middle_name = self.middle_name + name_array[j]
            if j < num_name_parts - 2:
                self.middle_name = self.middle_name + " "
                    
        if (num_name_parts > 1):
            self.last_name = name_array[num_name_parts-1]

    def parseAffiliation(self,profile):
        if ('history' in profile.content.keys() and profile.content['history']):
            history = profile.content['history'][0]
            self.institution = history['institution']['name']
            
            if ('country' in history['institution'].keys()):
                self.country_code = history['institution']['country']
                self.country = cc.convert(names=self.country_code, to='name')

            if ('city' in history['institution'].keys()):
                self.city = history['institution']['city']

            if ('stateProvince' in history['institution'].keys()):
                self.state = history['institution']['stateProvince']

        if ('preferredEmail' in profile.content.keys()):
            self.email = profile.content['preferredEmail']

    def printXML(self,author_number,contact_author):

      if not author_number or not contact_author:
        print("Author.getXML(author_number,contact_author); all arguments are required")
        return
      
      print("      <author>")
      
      if self.first_name:
        print("        <first_name>"+self.first_name+"</first_name>")
      else:
        print("        <first_name/>")

      if self.middle_name:
        print("        <middle_name>"+self.middle_name+"</middle_name>")
      else:
        print("        <middle_name/>")


      if self.last_name:
        print("        <last_name>"+self.last_name+"</last_name>")
      else:
        print("        <last_name/>")

      print("        <affiliations>")
      print("          <affiliation>")
      print("            <department/>")

      if self.institution:
        print("            <institution>"+self.institution+"</institution>")
      else:
        print("            <institution/>")

      if self.city:
        print("            <city>"+self.city+"</city>")
      else:
        print("            <city/>")

      if self.state:
        print("            <state_province>"+self.state+"</state_province>")
      else:
        print("            <state_province/>")

      if self.country:
        print("            <country>"+self.country+"</country>")
      else:
        print("            <country/>")

      print("            <sequence_no>1</sequence_no>")
        
      print("          </affiliation>")
      print("        </affiliations>")

      if self.email:
        print("        <email_address>"+self.email+"</email_address>")
      else:
        print("        <email_address/>")

      print("        <sequence_no>"+str(author_number)+"</sequence_no>")

      print("        <contact_author>"+contact_author+"</contact_author>")

      print("        <ACM_profile_id/>")
      print("        <ACM_client_no/>")
      print("        <ORCID/>")
      
      print("      </author>")
        
      return 0

    def getCSV(self,author_print_format=None):

        if not author_print_format or author_print_format == "short":
            return self.full_name

        # now, construct the longer format including emails
        author_long = self.full_name + " <"+self.email+">"
        
        return author_long
        
class Review:

    def __init__(self,text,technical_quality,significance,presentation,overall_rating,confidence):
        self.text = text
        self.technical_quality = technical_quality
        self.significance = significance
        self.presentation = presentation
        self.overall_rating = overall_rating
        self.confidence = confidence
        self.text_length = len(text)

    def getScore(self):
        return self.overall_rating

    def getText(self):
        return self.text

    def getTextLength(self):
        return self.text_length

    '''
    format: review text length, technical quality score, significance score, 
            presentation score, confidence, and overall rating
    '''
    def getFull(self):
        return str(self.text_length)+"\t"+str(self.technical_quality)+"\t"+str(self.significance)+"\t"+str(self.presentation)+"\t"+str(self.confidence)+"\t"+str(self.overall_rating)
