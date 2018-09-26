************************************************
.gov.br: Timeline
************************************************

.. contents:: Conteúdos
   :depth: 2

Introdução
-----------

Este complemento provê um tipo de conteúdo e tile para mostrar uma timeline.

Estado deste complemento
------------------------

O **brasil.gov.timeline** tem testes automatizados e, a cada alteração em seu
código os testes são executados pelo serviço Travis.

O estado atual dos testes pode ser visto nas imagens a seguir:

.. image:: http://img.shields.io/pypi/v/brasil.gov.timeline.svg
    :target: https://pypi.python.org/pypi/brasil.gov.timeline

.. image:: https://img.shields.io/travis/plonegovbr/brasil.gov.timeline/master.svg
    :target: http://travis-ci.org/plonegovbr/brasil.gov.timeline

.. image:: https://img.shields.io/coveralls/plonegovbr/brasil.gov.timeline/master.svg
    :target: https://coveralls.io/r/plonegovbr/brasil.gov.timeline

.. image:: https://img.shields.io/codacy/grade/77956b9df8a34087bc7ac4079f0e2ae3.svg
    :target: https://www.codacy.com/project/plonegovbr/brasil.gov.timeline/dashboard

Instalação
----------

Para habilitar a instalação deste complemento em um ambiente que utilize o buildout:

1. Editar o arquivo buildout.cfg (ou outro arquivo de configuração) e adicionar o pacote ``brasil.gov.agenda`` à lista de eggs da instalação::

        [buildout]
        ...
        eggs =
            brasil.gov.timeline

2. Após alterar o arquivo de configuração é necessário executar ''bin/buildout'', que atualizará sua instalação.

3. Reinicie o Plone

4. Acesse o painel de controle e instale o complemento **brasil.gov.timeline**.
