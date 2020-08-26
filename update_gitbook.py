#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

EXCLUDE = ('imgs', 'logo', '_books')

def get_issues_info():
    infos = {}
    for root, dirs, files in os.walk('.'):
        if root != '.' and not root.startswith('./.') \
                and root.startswith('./') and not root.startswith('./_'):
            category = root.replace('./', '').split('/')[0]
            if category in EXCLUDE:
                continue
            infos[category] = files
    return infos


def format_category(category, issue_files):
    '''
    * [git](git/README.md)
        * [git](git/git.issue.md)
        * [gitbook](git/gitbook.issue.md)
        * [github](git/github.issue.md)
    '''
    category_format = '* [{category}]({category}/README.md)\n'
    issue_format = '    * [{issue}]({category}/{issue}.issue.md)\n'
    data = []
    data.append(category_format.format(category=category))
    suffix = '.issue.md'
    for each in issue_files:
        if not each.endswith(suffix):
            continue
        issue = each.replace(suffix, '')
        data.append(issue_format.format(category=category, issue=issue))
    return ''.join(data)


def generate_summary():
    text = "# skill_issues\n\n平时开发时的经验积累，有高级用法，也有简单用法，都是干货。为的是增加开发效率！\n\n"
    issues_info = get_issues_info()
    for category, issue_files in sorted(issues_info.items()):
        text += format_category(category, sorted(issue_files))

    with open(os.path.join('.', 'SUMMARY.md'), 'w') as f:
        f.write(text)

if __name__ == '__main__':
    generate_summary()
