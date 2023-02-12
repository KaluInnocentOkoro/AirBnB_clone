#!/usr/bin/python3
"""Test cases"""
import unittest
import uuid
from datetime import datetime, timedelta
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id_is_unique(self):
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_attributes(self):
        """tests for object attributes"""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

        # Test creating from dictionary representation
        bm_dict = {
            'id': '12345678-1234-1234-1234-123456789abc',
            'created_at': (datetime.now() - timedelta(seconds=10)).isoformat(),
            'updated_at': (datetime.now() - timedelta(seconds=5)).isoformat(),
        }
        bm = BaseModel(**bm_dict)
        self.assertNotEqual(self.model.id, bm_dict['id'])
        self.assertNotEqual(
            bm.created_at,
            datetime.strptime(bm_dict['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        )
        self.assertNotEqual(
            bm.updated_at,
            datetime.strptime(bm_dict['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        )

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
        self.assertIn('created_at', result)
        self.assertIn('updated_at', result)


if __name__ == "__main__":
    unittest.main()
