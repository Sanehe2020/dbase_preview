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
 
# begin inserts
p = Prova(
        ano=2019,
        esfera='Estadual',
        banca='CESPE',
        tipo='CE',
        escolaridade='superior',
        area='direito',
        instituto='PGE',
        instituto_uf='AP',
        instituto_municipio='macapá',
        supercargo='Procurador',
        cargo='Procurador do Estado',
        ninscritos=3000,
        nota_max=70.00,
        corte = 65.00
    )

session.add(p)
session.commit()