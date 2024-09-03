#!/usr/local/bin/python3
supported_attrs = ('html_class', 'id')


def filter_attr(**attrs):
    return ' '.join(f'{key.split('_')[-1]}="{value}"'
                    for key, value in attrs.items() if key in supported_attrs)


def tag(tag, *args, **kwargs):
    attrs = filter_attr(**kwargs)
    return f'<{tag} {attrs}>{''.join(child for child in args)}</{tag}>'


EXPECTED_VALUE = '<p class="alert">\
<span >Curso de Python 3, por </span>\
<strong id="jf">Juracy Filho</strong>\
<span > e </span><strong id="ll">Leonardo Leitão</strong>\
<span >.</span>\
</p>'

if __name__ == '__main__':
    html = tag('p',
               tag('span', 'Curso de Python 3, por '),
               tag('strong', 'Juracy Filho', id='jf'),
               tag('span', ' e '),
               tag('strong', 'Leonardo Leitão', id='ll'),
               tag('span', '.'),
               html_class='alert')
    print(html)
    assert html == EXPECTED_VALUE
