import openreview
import client_object
import sys

client = client_object.client
venue_id = client_object.venue_id

venue_group = client.get_group(venue_id)

submissions = client.get_all_notes(invitation=f'{venue_id}/-/Submission',details='replies')

total_assignments = {}
complete_assignments = {}
no_reviews_done = ["~Ruofeng_Yang1",
"~Xiangyu_Liu4",
"~Andreas_Niskanen1",
"~Christian_Cabrera1",
"~Alessandro_Burigana1",
"~Thomas_C._Carroll1",
"~Chinmay_Sonar1",
"~Zichun_Zhong1",
"~Sarah_Kiden1",
"~Christophe_GUETTIER1",
"~YAN_ZHENG1",
"~Chairi_Kiourt1",
"~Jinhao_Liang1",
"~Cassia_Trojahn1",
"~Adina_Magda_Florea2",
"~Junichi_Suzuki1",
"~Qin_Yang2",
"~Jamal_Bentahar2",
"~Rik_Sengupta1",
"~Hirotaka_Ono1",
"~BRAHAMI_Menaouer1",
"~Mohamed_Tahar_Bennai1",
"~Maurice_Pagnucco1",
"~Fernando_Santos_Osório1",
"~Adrian_Agogino1",
"~Ladislau_Boloni1",
"~Nadin_Kökciyan1",
"~Matteo_Baldoni1",
"~Soumajyoti_Sarkar1",
"~Ramasuri_Narayanam2",
"~Yves_Lesperance1",
"~Claudia_Szabo1",
"~Filipe_Saraiva1",
"~Dongmo_Zhang1",
"~Evandro_de_Barros_Costa1",
"~Fengshuo_Bai1",
"~Tien_Anh_Mai1",
"~Yiqun_Chen3",
"~Marcos_de_Oliveira1",
"~Aron_Laszka1",
"~Monica_Tirea1",
"~Tiep_Le2",
"~Gauri_Vaidya1",
"~Ayan_Mukhopadhyay1",
"~Alessandro_Sapienza1",
"~Fuyuki_Ishikawa2",
"~Joris_Hulstijn1",
"~Paulo_Novais1",
"~Tomer_Ezra2",
"~Davide_Calvaresi1",
"~João_M._C._Sousa1",
"~Corrado_Santoro1",
"~Sergio_Alvarez-Napagao1",
"~Kai_Jin3",
"~Yì_N._Wáng2",
"~Trung_Thanh_Nguyen2",
"~Kazunori_Terada2",
"doanhbondy@gmail.com",
"~Wei_Pan2",
"~Tuan_Quang_Dam1",
"~Andrea_Baisero1",
"~Eduardo_Aoun_Tannuri1",
"~Kamel_Barkaoui1",
"~Rajith_Vidanaarachchi1",
"~Mark_A_Post1",
"~Dell'Acqua_Pierangelo1",
"~Antonino_Rotolo2",
"~Eduardo_Mena1",
"~Thanh_Vinh_Vo2",
"~Goreti_Marreiros1",
"~Jingqing_Ruan1",
"~Filip_Cano_Cordoba1",
"~Antoine_Zimmermann1",
"~Gautham_Das2",
"~Chengguang_Xu1",
"~Elias_Fernández_Domingos2",
"~Koen_Kok1",
"~Ting_Liu28",
"~Giovanni_Sartor1",
"~Rica_Gonen2",
"archie.chapman@uq.edu.au",
"~Roland_Yap1",
"~Federico_Tavella1",
"~Xu_Li32",
"~Ganesh_Ramanathan2",
"~Ocan_Sankur1",
"~Xiaolong_Liu7",
"~Helen_Harman2",
"~Elia_Pacioni1",
"~Xueguang_Lyu1",]

no_reviews=[]
for submission in submissions:
    if (not f'{venue_id}/-/Desk_Rejected_Submission' in submission.invitations):
        possible_issue = False
        number = submission.number
        try:
            r_ids = client.get_group(f'{venue_id}/Submission{number}/Reviewers').members
        except:
            continue
        for rev in r_ids:
            if rev in no_reviews_done:
                no_reviews.append(number)

no_reviews.sort()
       
last_issue = 0
count = 1
for issue in no_reviews:
    if (issue == last_issue):
        count = count + 1
        if (count == 3):
            print(issue)
    else:
        count = 1
        last_issue = issue
