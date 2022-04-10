# Write your MySQL query statement below
SELECT patient_id, patient_name, conditions From Patients 
WHERE conditions LIKE "% DIAB1%"
OR conditions like "DIAB1%"
                            
 