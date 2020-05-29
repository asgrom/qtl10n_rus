from PyQt5.QtCore import QTranslator
from PyQt5.QtWidgets import QApplication
import os

l18n_ru = os.path.abspath('/usr/share/qt5/tranlations')


def setupRussiaLang(app: QApplication):
    try:
        for file in os.listdir(l18n_ru):
            if file.startswith('qt') and file.endswith('_ru.qm'):
                translation = QTranslator(app)
                translation.load(os.path.join(l18n_ru, file))
                app.installTranslator(translation)
    except Exception as e:
        print('ERROR LOCALIZATION')
        print(e)
