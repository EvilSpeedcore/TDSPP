# -*- coding: cp1251 -*-

import sys
import uno
from logic.functions import make_elements, make_section_for_specification, make_section_for_list_of_elements
from logic.document import Specification, ListOfElements
from logic.exporter import Exporter
from logic.decorator import Decorator


def get_document_model():
    local_ctx = uno.getComponentContext()
    resolver = local_ctx.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local_ctx)
    ctx = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
    service_manager = ctx.ServiceManager
    desktop = service_manager.createInstanceWithContext("com.sun.star.frame.Desktop",ctx)
    model = desktop.getCurrentComponent()
    return model


def assemble_document(document):
    exporter = Exporter(document)
    exporter.export()
    decorator = Decorator(document, exporter.get_ranges())
    decorator.decorate()


def make_document():
    filename, doc_type = sys.argv[1:]
    elements = make_elements(filename)
    model = get_document_model()
    if doc_type == '1':
        section = make_section_for_specification(elements)
        specification = Specification(model, section)
        assemble_document(specification)
    elif doc_type == '2':
        section = make_section_for_list_of_elements(elements)
        list_of_elements = ListOfElements(model, section)
        assemble_document(list_of_elements)


if __name__ == '__main__':
    make_document()
