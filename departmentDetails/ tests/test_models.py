from django.test import TestCase
from departmentDetails.models import Level
from quizDetails.models import Quiz


class LevelTests(TestCase):
    def setUp(self):
        Level.objects.create(
            name='100'
        )

    def test_level_creation(self):
        """
        Testing an instance of a Level model
        created. Instance should return the 
        data of  name attribute as the '__str__'
        of the class, Level.
        """

        obj = Level.objects.get(pk=1)

        self.assertIsInstance(obj, Level)
        self.assertEqual(obj.__str__(), obj.name)

    def test_not_level_creation(self):
        """Testing an instance of a level model is not created.
        """
        obj = Level.objects.get(pk=1)
        not_obj = 'This is just a dummy word'

        self.assertNotIsInstance(not_obj, Level)
        self.assertNotEqual(obj.__str__(), not_obj)

    def test_data_for_instance_of_level_model(self):
        """
        Testing an instance data is correct
        """
        ins = Level.objects.get(pk=1)

        self.assertEqual(ins.name, '100')

    def test_data_not_for_instance_of_level_model(self):
        """
        Testing an instance data is not correct
        """
        ins = Level.objects.get(pk=1)

        self.assertNotEqual(ins.name, 'This is not your data')

    def test_get_subject_method(self):
        """
        get_subject method should return all the unique
        courses in caps 'BIOLOGY CHEMISTRY BIOCHEMISTRY'
        """
        ins = Level.objects.get(pk=1)
        quiz = Quiz.objects.create(level=ins, course_subject='Biology',
                                   course_title='Physical Biology', course_code='BIO101',
                                   number_of_question=30, time=10, required_score_to_pass=80)

        self.assertTrue(ins.get_subject())
        self.assertIn('BIOLOGY', ins.get_subject())

    def test_get_subject_method_not_work(self):
        """
        get_subject method should return an empty set if 
        Quiz object is not yet created.
        """
        ins = Level.objects.get(pk=1)

        self.assertFalse(ins.get_subject())
        self.assertEqual(set(), ins.get_subject())
