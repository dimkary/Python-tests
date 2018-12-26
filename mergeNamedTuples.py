#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 09:49:20 2018

@author: karips

Test from a recruitement company. Given several named tuples with medical 
records of a patient, merge them into one named tuple with all 
the corresponding fields
"""
from collections import namedtuple

class MedicalRecord:
    
    @staticmethod
    def merge(*records):
        """
        :param records: (varargs list of namedtuple) The patient details.
        :returns: (namedtuple) named Patient, containing details from all records, in entry order.
        """
        fields = []
        traits = []
        for i in records:
            fields.append(i._fields)
            counter = 0
            for k in i._fields:
                traits.append(i[counter])
                counter+=1
        fields = [item for sublist in fields for item in sublist]
        Patient = namedtuple('Patient', fields)
        patient = Patient._make(traits)
        return patient
    
PersonalDetails = namedtuple('PersonalDetails', ['date_of_birth','gender','height'])
personal_details = PersonalDetails(date_of_birth = '06-04-1972',
                                   gender = 'Male',
                                   height = 168)
                                   
Complexion = namedtuple('Complexion', ['eye_color', 'hair_color'])
complexion = Complexion(eye_color = 'Blue', hair_color = 'Black')


a=MedicalRecord.merge(personal_details, complexion)
