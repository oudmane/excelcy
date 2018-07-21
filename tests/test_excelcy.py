from excelcy import ExcelCy
from excelcy.storage import Config
from tests.test_base import BaseTestCase


class TestExcelCy(BaseTestCase):
    def test_readme_01(self):
        """ Test: code snippet found in README.rst """

        excelcy = ExcelCy()
        excelcy.storage.config = Config(nlp_base='en_core_web_sm', train_iteration=2, train_drop=0.2)
        train = excelcy.storage.train.add(text='Uber blew through $1 million a week')
        train.add(subtext='Uber', entity='ORG')
        excelcy.train()
        assert excelcy.nlp('Uber blew through $1 million a week').ents[0].label_ == 'ORG'

    def test_readme_02(self):
        """ Test: code snippet found in README.rst """

        excelcy = ExcelCy()
        excelcy.storage.config = Config(nlp_base='en_core_web_sm', train_iteration=2, train_drop=0.2)
        excelcy.storage.train.add(text='Robertus Johansyah is the maintainer ExcelCy')
        excelcy.storage.train.add(text='Who is the maintainer of ExcelCy? Robertus Johansyah, I think.')
        excelcy.storage.prepare.add(kind='phrase', value='Robertus Johansyah', entity='PERSON')
        excelcy.prepare()
        excelcy.train()
        assert excelcy.nlp('Robertus Johansyah is maintainer ExcelCy').ents[0].label_ == 'PERSON'
        assert excelcy.nlp('Who is the maintainer of ExcelCy? Robertus Johansyah, I think.').ents[1].label_ == 'PERSON'

    def test_readme_03(self):
        """ Test: code snippet found in README.rst """

        excelcy = ExcelCy()
        excelcy.storage.base_path = self.test_data_path
        excelcy.storage.config = Config(nlp_base='en_core_web_sm', train_iteration=2, train_drop=0.2)
        excelcy.storage.source.add(kind='text', value='Robertus Johansyah is the maintainer ExcelCy')
        excelcy.storage.source.add(kind='textract', value='source/test_source_01.txt')
        excelcy.storage.prepare.add(kind='phrase', value='Uber', entity='ORG')
        excelcy.storage.prepare.add(kind='phrase', value='Robertus Johansyah', entity='PERSON')
        excelcy.discover()
        excelcy.prepare()
        excelcy.train()
        assert excelcy.nlp('Uber blew through $1 million a week').ents[0].label_ == 'ORG'
        assert excelcy.nlp('Robertus Johansyah is maintainer ExcelCy').ents[0].label_ == 'PERSON'

    def test_readme_04(self):
        """ Test: code snippet found in README.rst """

        excelcy = ExcelCy()
        excelcy.storage.config = Config(nlp_base='en_core_web_sm', train_iteration=2, train_drop=0.2)
        excelcy.storage.source.add(kind='text', value='Robertus Johansyah is the maintainer ExcelCy')
        excelcy.discover()
        excelcy.storage.prepare.add(kind='phrase', value='Robertus Johansyah', entity='PERSON')
        excelcy.prepare()
        excelcy.train()
        assert excelcy.nlp('Robertus Johansyah is maintainer ExcelCy').ents[0].label_ == 'PERSON'

    def test_readme_05(self):
        """ Test: code snippet found in README.rst """

        self.assert_training(file_path='test_data_28.xlsx')

    def test_readme_06(self):
        """ Test: code snippet found in README.rst """

        excelcy = ExcelCy()
        excelcy.storage.config = Config(nlp_base='en_core_web_sm', train_iteration=2, train_drop=0.2)
        assert excelcy.nlp('Robertus Johansyah is maintainer ExcelCy').ents[0].text == 'Robertus'

        excelcy.storage.source.add(kind='text', value='Robertus Johansyah is the maintainer ExcelCy')
        excelcy.discover()
        excelcy.storage.prepare.add(kind='phrase', value='Robertus Johansyah', entity='PERSON')
        excelcy.prepare()
        excelcy.train()

        assert excelcy.nlp('Robertus Johansyah is maintainer ExcelCy').ents[0].text == 'Robertus Johansyah'
