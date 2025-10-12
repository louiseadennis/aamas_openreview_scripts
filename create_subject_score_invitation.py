import openreview
import client_object

# API V2
client = client_object.client

venue_id = client_object.venue_id

client.post_invitation_edit(
    invitations=f'{venue_id}/-/Edit',
    readers=[venue_id],
    writers=[venue_id],
    signatures=[venue_id],
    invitation=openreview.api.Invitation(
        id = f"{venue_id}/Reviewers/-/Subject_Score",
        invitees = [venue_id,"OpenReview.net/Support"],
        readers = [venue_id],
        writers = [venue_id],
        signatures = [venue_id],
        edge = {
                "id": {
                    "param": {
                        "withInvitation": f"{venue_id}/Reviewers/-/Subject_Score",
                        "optional": True
                    }
                },
                "ddate": {
                    "param": {
                        "range": [ 0, 9999999999999 ],
                        "optional": True,
                        "deletable": True
                    }
                },
                "cdate": {
                    "param": {
                        "range": [ 0, 9999999999999 ],
                        "optional": True,
                        "deletable": True
                    }
                },
                "readers": [
                    venue_id,
                    "${2/tail}"
                  ],
                  "nonreaders": [],
                  "writers": [
                    venue_id
                  ],
                "signatures": {
                    "param": {
                      "regex": f"{venue_id}$|{venue_id}/Program_Chairs",
                      "default": [
                        f"{venue_id}/Program_Chairs"
                      ]
                    }
                  },
                "head": {
                    "param": {
                      "type": "note",
                      "withInvitation": f"{venue_id}/-/Submission"
                    }
                  },
                "tail": {
                    "param": {
                      "type": "profile",
                      "options": {
                        "group": f"{venue_id}/Reviewers"
                      }
                    }
                  },
                "weight": {
                    "param": {
                      "minimum": -1
                    }
                  },
                "label": {
                    "param": {
                      "regex": ".*",
                      "optional": True,
                      "deletable": True
                    }
                  }
            }
    )
)
