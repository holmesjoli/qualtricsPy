# Qualtrics API

<!-- badges: start -->
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/47a551af52ee49cd8884d30bfe48f07a)](https://www.codacy.com/app/holmesjoli/qualtricsPy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=holmesjoli/qualtricsPy&amp;utm_campaign=Badge_Grade)
<!-- badges: end -->

## Config Files

1.  Update the qualtricsCredentials.yaml file
2.  Update the config.yaml file

## Example code

```yaml
copySurvey:
  id: 
  name: "NEW NAME"
getSurvey:
  id: 
updateSurvey:
  id: 
  name: "NEW NAME"
  active: False
createQuestion:
  id: 
  question:
    QuestionText: "<div> </div>\n\n<div> </div>\n\n<div> </div>\n\n<table class=\"UserTable\" border=\"2px\">\n <tbody>\n  <tr>\n   <td> </td>\n   <td style=\"font-weight: bolder; font-size: 14px; text-align: center;\">Option 1</td>\n   <td style=\"font-weight: bolder; font-size: 14px; text-align: center;\">Option 2</td>\n   <td style=\"font-weight: bolder; font-size: 14px; text-align: center;\">None</td>\n  </tr>\n  <tr>\n   <td style=\"font-weight: bolder; font-size: 14px;\">Program Description</td>\n   <td><span style=\"font-size:12.0pt\">A {}-year, 45 credit, evening program that would allow you to work while you study. </span></td>\n   <td><span style=\"font-size:12.0pt\">A {}-year, 30 credit, day program that would not allow you to work while you study.</span></td>\n   <td rowspan=\"3\">I prefer not to enroll in any of these two programs.</td>\n  </tr>\n  <tr>\n   <td style=\"font-weight: bolder; font-size: 14px;\">Tuition</td>\n   <td>${} per year; total cost is ${}.</td>\n   <td>${} per year; total cost is ${}.</td>\n  </tr>\n  <tr>\n   <td style=\"font-weight: bolder; font-size: 14px;\">Expected Salary Increase</td>\n   <td>${}</td>\n   <td>${}</td>\n  </tr>\n  <tr>\n   <td> </td>\n   <td><input class=\"sneakyButton\" id=\"1\" name=\"craigsmom\" type=\"radio\"></td>\n   <td><input class=\"sneakyButton\" id=\"2\" name=\"craigsmom\" type=\"radio\"></td>\n   <td><input class=\"sneakyButton\" id=\"3\" name=\"craigsmom\" type=\"radio\"></td>\n  </tr>\n </tbody>\n</table><style type=\"text/css\">.QuestionText{{\ntext-align: center;\n}}\n.UserTable td{{\npadding: 5px;\nwidth: 650px;\n}}\n.LargeText{{\nfont-weight: bolder;\n}}\n</style>"
    QuestionType: DB
    Selector: TB
    SubSelector: Null


```

```python
import pandas as pd

from utilsPy.config import read_yaml

from qualtricsPy.copySurvey import copySurvey
from qualtricsPy.createQuestion import createQuestion
from qualtricsPy.updateSurvey import updateSurvey
from qualtricsPy.getSurvey import getSurvey


class config(object):

    def __init__(self):
        """
        Initiates the configuration class
        """
        self.config = read_yaml("config.yaml")
        self.copySurvey = self.config["copySurvey"]
        self.getSurvey = self.config["getSurvey"]
        self.updateSurvey = self.config["updateSurvey"]
        self.createQuestion = self.config["addQuestion"]


class main(config):

    def __init__(self):

        config.__init__(self)
        copySurvey(self.copySurvey)
        getSurvey(self.getSurvey)
        createQuestion(self.createQuestion)
        updateSurvey(self.updateSurvey)

if __name__ == "__main__":

    main()
```