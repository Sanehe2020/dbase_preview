import os
import sys
from utils import grep
from sqlalchemy import Table, Column, ForeignKey, Integer, String, Float, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
 
Base = declarative_base()

#relação entre assertiva e Lei
leis = Table('leis', Base.metadata,
    Column('assertiva_id', Integer, ForeignKey('assertiva.id'), primary_key=True),
    Column('lei_id', Integer, ForeignKey('lei.id'), primary_key=True)
)

#relação entre assertiva e OJ
ojs = Table('ojs', Base.metadata,
    Column('assertiva_id', Integer, ForeignKey('assertiva.id'), primary_key=True),
    Column('oj_id', Integer, ForeignKey('oj.id'), primary_key=True)
)

#relação entre assertiva e Sumula
sumulas = Table('sumulas', Base.metadata,
    Column('assertiva_id', Integer, ForeignKey('assertiva.id'), primary_key=True),
    Column('sumula_id', Integer, ForeignKey('sumula.id'), primary_key=True)
)

#relação entre assertiva e Enunciado
enunciados = Table('enunciados', Base.metadata,
    Column('assertiva_id', Integer, ForeignKey('assertiva.id'), primary_key=True),
    Column('enunciado_id', Integer, ForeignKey('enunciado.id'), primary_key=True)
)

class Prova(Base):
    __tablename__ = 'prova'
    id = Column(Integer, autoincrement=True, primary_key=True)
    ano = Column(String(8))
    esfera = Column(String(128))
    banca = Column(String(128))
    tipo = Column(String(128)) #Certo errado / de marcar
    escolaridade = Column(String(128))
    area = Column(String(128))
    instituto = Column(String(128))
    instituto_uf = Column(String(2))
    instituto_municipio = Column(String(128))
    supercargo = Column(String(128))
    cargo = Column(String(128))
    ninscritos = Column(Integer)
    nota_max = Column(Float)
    corte = Column(Float)

    def __repr__(self):
        identification = '<Prova {} - {} - {} - {}>'.format(self.instituto, self.cargo, self.banca, self.ano)
        
        if self.esfera.lower() == 'municipal':
            identification = '<Prova {} - {} - {}/{} - {} - {}>'.format(self.instituto, self.cargo, 
                              self.instituto_municipio, self.instituto_uf, self.banca, self.ano)
        
        if self.esfera.lower() == 'estadual':
            identification = '<Prova {}/{} - {} - {} - {}>'.format(self.instituto, self.instituto_uf, self.cargo, 
                              self.banca, self.ano)

        return identification

class Questao(Base):
    __tablename__ = 'questao'
    id = Column(Integer, autoincrement=True, primary_key=True)
    prova_id = Column(Integer, ForeignKey('prova.id'))
    numero = Column(Integer)
    materia = Column(String(128))
    corpo = Column(Text)
    anulada = Column(Boolean, default=False)
    desatualizada = Column(Boolean, default=False)
    obs = Column(Text)
    #relationships
    prova = relationship('Prova', backref='questoes', lazy=True)

    def __repr__(self):
        text = grep(self.corpo, 30)+"..."
        return '<Questao {} - {}>'.format(str(self.numero), text) 

    def lista_assertivas(self):
        asserts = self.assertivas
        text = self.corpo+'\n'
        for i in asserts:
            text+=i.corpo
            text+='\n'
        return '<Questao\n:  {}>'.format(text)

class Assertiva(Base):
    __tablename__ = 'assertiva'
    id = Column(Integer, autoincrement=True, primary_key=True)
    questao_id = Column(Integer, ForeignKey('questao.id'))
    letra = Column(String(2))
    corpo = Column(Text)
    correta = Column(Boolean, nullable=False)
    jurisprudencia = Column(Text)
    doutrina = Column(Text)
    obs = Column(Text)
    #relationships
    questao = relationship('Questao', backref='assertivas', lazy=True)

    leis = relationship('Lei', secondary=leis, lazy='subquery',
                            backref=backref('assertivas', lazy=True))

    ojs = relationship('Oj', secondary=ojs, lazy='subquery',
                            backref=backref('assertivas', lazy=True))

    sumulas = relationship('Sumula', secondary=sumulas, lazy='subquery',
                            backref=backref('assertivas', lazy=True))

    enunciados = relationship('Enunciado', secondary=enunciados, lazy='subquery',
                            backref=backref('assertivas', lazy=True))

    def __repr__(self):
        return '<Q{}.{} - {}>'.format(str(self.questao.numero), self.letra, grep(self.corpo, 30)+"...")

class Oj(Base):
    __tablename__ = 'oj'
    id = Column(Integer, autoincrement=True, primary_key=True)
    entidade = Column(String(128))
    numero = Column(Integer)
    cancelada = Column(Boolean, nullable=False)

    def __repr__(self):
        return '<OJ {} n. {}>'.format(self.entidade, str(self.numero))

class Sumula(Base):
    __tablename__ = 'sumula'
    id = Column(Integer, autoincrement=True, primary_key=True)
    entidade = Column(String(128))
    numero = Column(Integer)
    vinculante = Column(Boolean)
    cancelada = Column(Boolean)

    def __repr__(self):
        vinc = ''
        if (self.vinculante):
            vinc = 'vinculante'
        return '<Sumula {} {} n. {}>'.format(vinc, self.orgao, str(self.numero))

class Enunciado(Base):
    __tablename__ = 'enunciado'
    id = Column(Integer, autoincrement=True, primary_key=True)
    entidade = Column(String(128))
    numero = Column(Integer)
    cancelada = Column(Boolean, nullable=False)

    def __repr__(self):
        return '<Enunciado {} n. {}>'.format(self.entidade, str(self.numero))

class Lei(Base):
    __tablename__ = 'lei'
    id = Column(Integer, autoincrement=True, primary_key=True)
    esfera = Column(String(128))
    uf = Column(String(2))
    municipio = Column(String(128))
    tipo = Column(String(128))
    diploma = Column(Integer)
    ano = Column(Integer)
    livro = Column(String(128))
    titulo = Column(String(128))
    capitulo = Column(String(128))
    secao = Column(String(128))
    subsecao = Column(String(128))
    artigo = Column(String(8))
    paragrafo = Column(String(8))
    inciso = Column(String(8))
    alinea = Column(String(8))
    alterada = Column(Boolean)

    #relationships
    alteracoes = relationship('LeiAlt', backref='lei', lazy=True)

    def __repr__(self):
        placement = 'art. {}'.format(self.artigo)
        if not self.paragrafo and not self.inciso and not self.alinea:
            placement+=', caput'

        elif self.paragrafo and not self.inciso and not self.alinea:
            placement=', paragrafo único'

        elif self.paragrafo:
            placement+=', parágrafo {}'.format(self.paragrafo)
            if self.inciso:
                placement+=', inciso {}'.format(self.inciso)
            if self.alinea:
                placement+=', alinea {}'.format(self.alinea)
            

        location=''
        if self.esfera.lower() == 'municipal':
            location = ' - {}/{}'.format(self.municipio, self.uf)
        if self.esfera.lower() == 'estadual':
            location = ' - {}'.format(self.uf)

        return '<{} {} n. {}, {} {}>'.format(self.tipo, self.esfera, str(self.diploma), placement, location)

class LeiAlt(Base):
    __tablename__='lei_alt'
    id = Column(Integer, autoincrement=True, primary_key=True)
    lei_id = Column(Integer, ForeignKey('lei.id'))
    diploma = Column(Integer)
    ano = Column(Integer)                                                                        
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///smartlegis.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)