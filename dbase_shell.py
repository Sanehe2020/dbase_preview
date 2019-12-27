from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dbase_create import Prova, Questao, Assertiva, Oj, Sumula, Enunciado, Lei, LeiAlt

Base = declarative_base()

engine = create_engine('sqlite:///smartlegis.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

l1 = Lei(
        esfera='Federal',
        tipo='Lei Complementar',
        diploma=8666,
        ano=1993,
        artigo='1o',
        paragrafo='3o',
        inciso='V',
        alinea='d',
        alterada=False
)

l2 = Lei(
        esfera='Estadual',
        uf='AP',
        tipo='Decreto',
        diploma=66,
        ano=2010,
        artigo='6o',
        paragrafo='9o',
        inciso='I',
        alinea='a',
        alterada=False
)

l3 = Lei(
        esfera='Municipal',
        uf='AP',
        municipio='Santana',
        tipo='Lei de Saul',
        diploma=50,
        ano=2020,
        artigo='6o',
        paragrafo='9o',
        inciso='I',
        alinea='a',
        alterada=False
)

p1 = Prova(
        ano=2019,
        esfera='Federal',
        banca='CESPE',
        tipo='CE',
        escolaridade='superior',
        area='direito',
        instituto='PFN',
        supercargo='Procurador',
        cargo='Procurador Federal',
        ninscritos=3000,
        nota_max=70.00,
        corte = 65.00
)

p2 = Prova(
        ano=2019,
        esfera='Estadual',
        banca='CESPE',
        tipo='CE',
        escolaridade='superior',
        area='direito',
        instituto='PGE',
        instituto_uf='AP',
        supercargo='Procurador',
        cargo='Procurador Estadual',
        ninscritos=3000,
        nota_max=70.00,
        corte = 65.00
)

p3 = Prova(
        ano=2019,
        esfera='Municipal',
        banca='CESPE',
        tipo='CE',
        escolaridade='superior',
        area='direito',
        instituto='PGM',
        instituto_uf='AP',
        instituto_municipio='Macapá',
        supercargo='Procurador',
        cargo='Procurador Municipal',
        ninscritos=3000,
        nota_max=70.00,
        corte = 65.00
)

q1 = Questao(
    numero=1,
    materia='direito constitucional',
    corpo='''essa é uma questão de teste''',
    anulada=False,
    desatualizada=False,
    prova=p1
)

a1 = Assertiva(
        letra='a',
        corpo='corpo da assertiva a',
        correta = True,
        questao=q1, 
        leis=[l1,l2]
)

a2 = Assertiva(
        letra='b',
        corpo='corpo da assertiva b',
        correta = False,
        questao=q1 
)

a3 = Assertiva(
        letra='c',
        corpo='corpo da assertiva c',
        correta = False,
        questao=q1 
)

a4 = Assertiva(
        letra='d',
        corpo='corpo da assertiva d',
        correta = False,
        questao=q1 
)

a5 = Assertiva(
        letra='e',
        corpo='corpo da assertiva e',
        correta = False,
        questao=q1
)