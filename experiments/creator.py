def createApplicant(app):
    # (str)->(Applicant __init__)
    # takes the raw html from app, parses it and creates an applicant object with a unique id

    info = parse(app)

    # return Applicant(info)


# def parse(object):
#     # (str)->(dict)
#     # goes through formated html document and returns a dict to create Applicant object
#     sauce = object.bs
#     info = {
#     'name':,
#     'ip':,
#     'appdate':,
#     'status':,
#     'game':,
#     'firstreg':,
#     'why':,
#     'age':,
#     'live':,
#     'software':,
#     'rules':,
#     'events':,
#     '[findout , fother]':,
#     'steam':,
#     '[nco , acceptdate]':,
#
#     }


