# coding: utf-8

"""
    FlashBlade Management API

    The management APIs of FlashBlade.

    OpenAPI spec version: beta

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import json
import unittest

import environment
from environment import HOST, API_TOKEN
from purity_fb import *
from utils import *

DEMO_LIST = 'test_list'
DEMO_CREATE = 'test_create'


def dl_name(i):
    return DEMO_LIST + '_' + str(i)


def dc_name(i):
    return DEMO_CREATE + '_' + str(i)

class TestFileSystemsApi(unittest.TestCase):
    """ FileSystemsApi unit test stubs """

    def setUp(self):
        self.versions = environment.get_test_versions(HOST)
        self.latest = self.versions[-1]
        self.purity_fb = {}
        self.file_systems = {}

        for version in self.versions:
            self.purity_fb[version] = PurityFb(HOST, version=version)
            self.purity_fb[version].disable_verify_ssl()
            res = self.purity_fb[version].login(API_TOKEN)
            self.assertTrue(res == 200)
            self.file_systems[version] = self.purity_fb[version].file_systems

        self.cleanUp()
        for i in range(len(self.versions)):
            fs = FileSystem()
            fs.name = DEMO_LIST + '_' + str(i)
            fs.nfs = NfsRule(enabled=True)
            fs.provisioned = 1000
            self.file_systems[self.latest].create_file_systems(file_system=fs)
            fs.name = DEMO_CREATE + '_' + str(i)
            self.file_systems[self.latest].create_file_systems(file_system=fs)

    def tearDown(self):
        self.cleanUp()
        for version in self.versions:
            self.purity_fb[version].logout()

    def cleanUp(self):
        filter = 'name=\"' + DEMO_LIST + '*\" or name=\"' + DEMO_CREATE + '*\"'
        res = self.file_systems[self.latest].list_file_systems(filter=filter)
        for fs in res.items:
            attr = FileSystem()
            attr.nfs = NfsRule(enabled=False)
            attr.http = ProtocolRule(enabled=False)
            attr.smb = ProtocolRule(enabled=False)
            attr.destroyed = True
            self.file_systems[self.latest].update_file_systems(name=fs.name, attributes=attr)
            self.file_systems[self.latest].delete_file_systems(name=fs.name)

    def test_list_basic(self):
        for version in self.versions:
            print('LIST all file systems using API v{}\n'.format(version))
            res = self.file_systems[version].list_file_systems(limit=50)
            if DEBUG:
                print_list(res.items)
            check_is_list_of(res.items, FileSystem)

            names = [dl_name(0), dl_name(1)]
            print('\nLIST file systems by names {} using API v{}\n'.format(names, version))
            res = self.file_systems[version].list_file_systems(names=names)
            if DEBUG:
                print_list(res.items)

            filter_str = 'name = \'' + DEMO_LIST + '*\''
            print('\nLIST file systems by filter {} using API v{}\n'.format(filter_str, version))
            res = self.file_systems[version].list_file_systems(filter=filter_str)
            if DEBUG:
                print_list(res.items)
            check_is_list_of(res.items, FileSystem)

            print('\nCREATE file system {} using API v{}\n'.format(DEMO_CREATE, version))
            fs = FileSystem()
            fs.name = DEMO_CREATE
            fs.provisioned = "300000"
            try:
                res = self.file_systems[version].create_file_systems(file_system=fs)
            except:
                pass
            if DEBUG:
                print_list(res.items)
            check_is_list_of(res.items, FileSystem)

    def test_filter(self):
        # ----------- test FILTER ------------
        for version in self.versions:
            print('\nLIST file system by filter using API v{}\n'.format(version))

            filter_str = 'name = \'' + DEMO_CREATE + '*\''
            list_by_filter(self.file_systems[version].list_file_systems, filter_str, FileSystem)

            filter_str = 'name = \'' + DEMO_LIST + '*\' and not(contains(name, \'2\'))' + ' and created > 1456000'
            list_by_filter(self.file_systems[version].list_file_systems, filter_str, FileSystem)

    def test_sort(self):
        # ------ test SORT ----
        for version in self.versions:
            print('\nLIST file system and sort using API v{}\n'.format(version))
            list_and_sort(self.file_systems[version].list_file_systems, 'name', FileSystem)
            list_and_sort(self.file_systems[version].list_file_systems, '(natural)', FileSystem)
            list_and_sort(self.file_systems[version].list_file_systems, 'name-', FileSystem)
            list_and_sort(self.file_systems[version].list_file_systems, 'provisioned', FileSystem)
            list_and_sort(self.file_systems[version].list_file_systems, 'provisioned-', FileSystem)
            list_and_sort(self.file_systems[version].list_file_systems, 'smb.enabled', FileSystem)

    def test_start(self):
        # ------ test START ----
        for version in self.versions:
            print('\nLIST file system by start using API v{}\n'.format(version))
            list_by_start(self.file_systems[version].list_file_systems, 1, FileSystem)
            list_by_start(self.file_systems[version].list_file_systems, 2, FileSystem)

    def test_limit(self):
        # ------ test LIMIT ----
        for version in self.versions:
            print('\nLIST file system by limit using API v{}\n'.format(version))
            list_by_limit(self.file_systems[version].list_file_systems, 0, FileSystem)
            list_by_limit(self.file_systems[version].list_file_systems, 1, FileSystem)
            list_by_limit(self.file_systems[version].list_file_systems, 2, FileSystem)
            list_by_limit(self.file_systems[version].list_file_systems, 5, FileSystem)

    def test_token(self):
        # ------ test TOKEN ----
        for version in self.versions:
            print('\nLIST file system by token using API v{}\n'.format(version))
            res = list_by_limit(self.file_systems[version].list_file_systems, 1, FileSystem)
            token = res.pagination_info.continuation_token
            list_by_token(self.file_systems[version].list_file_systems, token, FileSystem)

    def test_combined(self):
        for version in self.versions:
            print('\nLIST file system by combined parameters using API v{}\n'.format(version))
            print('\nLIST by start, limit, filter\n')
            res = self.file_systems[version].list_file_systems(start=1, limit=3,
                                                               filter='name = \'' + DEMO_CREATE + '*\'')
            if DEBUG:
                print_list(res.items)
            check_is_list_of(res.items, FileSystem)

    def test_create(self):
        i = 0
        for version in self.versions:
            print('\nCREATE file system using API v{}\n'.format(version))
            name = DEMO_CREATE + '_create_' + str(i)
            i += 1
            size = 10000 * i
            fs_obj = FileSystem(name=name, provisioned=size)
            res = self.file_systems[version].create_file_systems(file_system=fs_obj)
            check_is_list_of(res.items, FileSystem)
            created_fs = res.items[0]
            self.assertTrue(created_fs.name == name)
            self.assertTrue(created_fs.provisioned == size)

    def test_update(self):
        i = 0
        for version in self.versions:
            print('\nUPDATE file system using API v{}\n'.format(version))
            name = DEMO_CREATE + '_' + str(i)
            i += 1
            size = 10000
            fs_attr = FileSystem()
            fs_attr.provisioned = size
            res = self.file_systems[version].update_file_systems(name=name, attributes=fs_attr)
            check_is_list_of(res.items, FileSystem)
            updated_fs = res.items[0]
            self.assertTrue(updated_fs.name == name)
            self.assertTrue(updated_fs.provisioned == size)

    def test_destroy(self):
        i = 0
        for version in self.versions:
            print('\nDESTROY file system using API v{}\n'.format(version))
            name = DEMO_CREATE + '_' + str(i)
            i += 1
            try:
                attr = FileSystem(destroyed=True, nfs=NfsRule(enabled=False), http=ProtocolRule(enabled=False),
                                  smb=ProtocolRule(enabled=False))
                # destroy file system
                res = self.file_systems[version].update_file_systems(name=name, attributes=attr)
                check_is_list_of(res.items, FileSystem)
                updated_fs = res.items[0]
                self.assertEqual(updated_fs.name, name)
                self.assertTrue(updated_fs.destroyed)
                attr = FileSystem(destroyed=False)
                # recover file system
                res = self.file_systems[version].update_file_systems(name=name, attributes=attr)
                check_is_list_of(res.items, FileSystem)
                updated_fs = res.items[0]
                self.assertEqual(updated_fs.name, name)
                self.assertFalse(updated_fs.destroyed)
            except rest.ApiException as error:
                self.assertEqual(version, '1.0')
                self.assertEqual(error.status, 400)
                body = json.loads(error.body)
                self.assertEqual(body['message'], 'invalid body parameter: destroyed')

if __name__ == '__main__':
    unittest.main()