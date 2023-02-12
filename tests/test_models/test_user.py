#!/usr/bin/python3
"""Test cases"""
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id_is_str(self):
        self.assertIsInstance(self.model.id, str)

    def test_id_is_unique(self):
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_attributes(self):
        """tests for object attributes"""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        updated_at = self.model.updated_at
        self.model.save()
        self.assertEqual(updated_at, self.model.updated_at)

    def test_to_dict_contains_class(self):
        self.assertIn("__class__", self.model.to_dict())

    def test_to_dict_contains_created_at(self):
        self.assertIn("created_at", self.model.to_dict())

    def test_to_dict_contains_updated_at(self):
        self.assertIn("updated_at", self.model.to_dict())

    def test_to_dict(self):
        """tests for to_dict method"""
        result = self.model.to_dict()
        self.assertIsInstance(result["created_at"], str)
        self.assertIsInstance(result["updated_at"], str)
        self.assertEqual(result["__class__"], "BaseModel")
        self.assertEqual(result["id"], self.model.id)


if __name__ == "__main__":
    unittest.main()
