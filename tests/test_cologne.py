import mock
import pytest
import six

import oparl
import oparl.objects

system = oparl.from_id('https://buergerinfo.stadt-koeln.de/oparl/system')

for body in system['body']:
    print(body['name'])

    # grab people
    for person in body['person']:
        print(person['name'])


