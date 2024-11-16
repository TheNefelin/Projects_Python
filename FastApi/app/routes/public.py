from fastapi import APIRouter
from typing import List
import asyncio

from app.mssql import execute_sp
from app.models import Projects, Links, Youtube

router = APIRouter(prefix="/public", tags=["public"])

@router.get("/projects", response_model = List[Projects])
async def get_projects():
  projects_data, pro_tec_data, pro_lan_data, technologies_data, languages_data = await asyncio.gather(
    execute_sp("PF_Proyecto_GetAll", ()),
    execute_sp("PF_ProTec_GetAll", ()),
    execute_sp("PF_ProLeng_GetAll", ()),
    execute_sp("PF_Tecnologia_GetAll", ()),
    execute_sp("PF_Lenguaje_GetAll", ())
  )

  projects = []

  for project in projects_data:
    technologies = [
      tech for tech in technologies_data if tech['Id'] in [
        pro_tec['Id_Tecnologia'] for pro_tec in pro_tec_data if pro_tec['Id_Proyecto'] == project['Id']
      ]
    ]

    languages = [
      lang for lang in languages_data if lang['Id'] in [
        pro_lan['Id_Lenguaje'] for pro_lan in pro_lan_data if pro_lan['Id_Proyecto'] == project['Id']
      ]
    ]

    projects.append(Projects(
        Id = project['Id'],
        Nombre = project['Nombre'],
        ImgUrl = project['ImgUrl'],
        Technologies = technologies,
        Languages = languages
    ))

  return projects

@router.get("/enlaces", response_model = List[Links])
async def get_links():
  linksgrp_data, links_data = await asyncio.gather(
    execute_sp("PF_EnlaceGrp_GetAll", ()),
    execute_sp("PF_Enlace_GetAll", ())
  )

  links = []

  for linksgrp in linksgrp_data:
    urls = [link for link in links_data if link['Id_EnlaceGrp'] == linksgrp['Id']]
   
    links.append(Links(
      Id = linksgrp['Id'],
      Nombre = linksgrp['Nombre'],
      Estado = linksgrp['Estado'],
      Urls = urls
    ))

  return links

@router.get("/youtubes", response_model = List[Youtube])
async def get_youtube():
  return await execute_sp("PF_Youtube_GetAll", ())
