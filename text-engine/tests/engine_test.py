import unittest
from src.engine import EtcherEngine

class TestEtcherEngine(unittest.TestCase):
    def setUp(self):
        self.engine = EtcherEngine()

    def test_add_text(self):
        self.engine.add_text("Hello")
        self.engine.add_text("World")
        self.assertEqual(self.engine.get_state(), "Hello World")

    def test_undo(self):
        self.engine.add_text("Hello")
        self.engine.add_text("World")
        state_after_undo = self.engine.undo()
        self.assertEqual(state_after_undo, "Hello")
        state_after_second_undo = self.engine.undo()
        self.assertEqual(state_after_second_undo, "")
        state_after_third_undo = self.engine.undo()
        self.assertIsNone(state_after_third_undo)

    def test_redo(self):
        self.engine.add_text("Hello")
        self.engine.add_text("World")
        self.engine.undo()  # Undo "World"
        state_after_redo = self.engine.redo()
        self.assertEqual(state_after_redo, "Hello World")
        state_after_second_redo = self.engine.redo()
        self.assertIsNone(state_after_second_redo)

    def test_undo_redo_sequence(self):
        self.engine.add_text("A")
        self.engine.add_text("B")
        self.engine.add_text("C")
        
        self.engine.undo()  # Remove C
        self.assertEqual(self.engine.get_state(), "A B")
        
        self.engine.undo()  # Remove B
        self.assertEqual(self.engine.get_state(), "A")
        
        self.engine.redo()  # Re-add B
        self.assertEqual(self.engine.get_state(), "A B")
        
        self.engine.add_text("D")  # Add D, should clear redo history
        self.assertEqual(self.engine.get_state(), "A B D")
        
        redo_result = self.engine.redo()  # Should be None since redo history is cleared
        self.assertIsNone(redo_result)