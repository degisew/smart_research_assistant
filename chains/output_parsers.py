from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser


class OutputParser(BaseModel):
    summary: str = Field(description="A brief overview of the company")
    team_background: str = Field(
        description="Key facts about the company's team and their background")
    competitors: list[str] = Field(
        description="Names of it's top 5 competitors in the industry")
    questions: list[str] = Field(
        description="Three insightful questions to ask the CEO or founder")

    def to_dict(self):
        return {
            "summary": self.summary,
            "team_background": self.team_background,
            "competitors": self.competitors,
            "questions": self.questions
        }


summary_parser = PydanticOutputParser(pydantic_object=OutputParser)
