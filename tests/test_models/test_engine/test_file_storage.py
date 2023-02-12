#!/usr/bin/python3
"""Test cases for storage"""
import os
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.obj = BaseModel()

    def test_all(self):
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        self.storage.new(self.obj)
        key = "{}.{}".format(self.obj.__class__.__name__, self.obj.id)
        self.assertIn(key, self.storage.all().keys())

    def test_save(self):
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        self.storage.save()
        self.storage.reload()
        self.assertEqual(self.storage.all(), self.storage.all())

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()

