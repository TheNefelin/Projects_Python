from pydantic import BaseModel

class Project(BaseModel):
  Id: int
  Nombre: str
  ImgUrl: str

class Technologie(BaseModel):
  Id: int
  Nombre: str
  ImgUrl: str

class Language(BaseModel):
  Id: int
  Nombre: str
  ImgUrl: str

class LinkGrp(BaseModel):
  Id: int
  Nombre: str
  Estado: bool

class Link(BaseModel):
  Id: int
  Nombre: str
  EnlaceUrl: str
  Estado: bool
  Id_EnlaceGrp: int

class Youtube(BaseModel):
  Id: int
  Nombre: str
  Embed: str

class Projects(BaseModel):
  Id: int
  Nombre: str
  ImgUrl: str
  Technologies: list[Technologie]
  Languages: list[Language]
  
class Links(BaseModel):
  Id: int
  Nombre: str
  Estado: bool
  Urls: list[Link]
