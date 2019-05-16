from qualtricsPy.utils import params, config
from qualtricsPy.apiVerbs import post


class createQuestionParams(params, config):

    def __init__(self):
        """
        Initializes the create question parameters
        """
        params.__init__(self)
        config.__init__(self)
        self.surveyId = self.addQuestion["id"]
        self.endpoint = "https://{}.qualtrics.com/API/v3/survey-definitions/{}/questions"
        self.endpoint = self.endpoint.format(self.dataCenter, self.surveyId)
        self.data = self.addQuestion["qs"]["q1"]
        self.headers = {"accept": "application/json",
                        "content-type": "application/json"}
        self.headers.update(self.authHeader)


class createQuestion(createQuestionParams):

    def __init__(self):
        """
        Creates a new question in the specified survey
        """
        createQuestionParams.__init__(self)
        post(self.endpoint, self.data, self.headers)
