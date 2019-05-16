# Qualtrics API

<!-- badges: start -->
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/47a551af52ee49cd8884d30bfe48f07a)](https://www.codacy.com/app/holmesjoli/qualtricsPy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=holmesjoli/qualtricsPy&amp;utm_campaign=Badge_Grade)
<!-- badges: end -->

## Config Files

1.  Update the qualtricsCredentials.yaml file
2.  Update the config.yaml file

## Example code

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

        self.mp = pd.read_csv("C:/Users/jh111/Projects/Packages/Python/qualtrics_automation/masters_program/master_program.csv")


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