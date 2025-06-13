#!/usr/bin/env python3
"""
Test script to verify the new patient structure where _id is the numeroCedula
"""

import asyncio
import json
from datetime import datetime
from app.config.database import get_database
from app.models.paciente import PacienteCreate, Paciente

async def test_patient_structure():
    """Test creating a patient with the new structure"""
    db = get_database()
    
    # Test data matching the required structure
    test_patient_data = {
        "numeroCedula": "12345678",
        "nombrePaciente": "Dasd Asd",
        "sexo": "masculino",
        "edad": 12,
        "entidad": "MINSA",
        "tipoAtencion": "ambulatorio",
        "observaciones": "sdasd"
    }
    
    print("Testing new patient structure...")
    print(f"Input data: {json.dumps(test_patient_data, indent=2)}")
    
    try:
        # Create PacienteCreate instance
        paciente_create = PacienteCreate(**test_patient_data)
        print(f"✓ PacienteCreate validation passed")
        
        # Simulate the creation process from the route
        paciente_dict = paciente_create.dict(exclude={"numeroCedula"})
        paciente_dict["_id"] = paciente_create.numeroCedula
        paciente_dict["fecha_creacion"] = datetime.utcnow()
        
        print(f"Document to be inserted: {json.dumps(paciente_dict, default=str, indent=2)}")
        
        # Check if patient already exists (cleanup first)
        await db.pacientes.delete_one({"_id": test_patient_data["numeroCedula"]})
        
        # Insert the patient
        result = await db.pacientes.insert_one(paciente_dict)
        print(f"✓ Patient inserted with _id: {result.inserted_id}")
        
        # Retrieve the patient
        retrieved_patient = await db.pacientes.find_one({"_id": test_patient_data["numeroCedula"]})
        
        if retrieved_patient:
            retrieved_patient["id"] = retrieved_patient["_id"]
            print(f"✓ Patient retrieved successfully")
            print(f"Retrieved document: {json.dumps(retrieved_patient, default=str, indent=2)}")
            
            # Verify the structure matches the expected format
            expected_structure = {
                "_id": test_patient_data["numeroCedula"],
                "nombrePaciente": test_patient_data["nombrePaciente"],
                "sexo": test_patient_data["sexo"],
                "edad": test_patient_data["edad"],
                "entidad": test_patient_data["entidad"],
                "tipoAtencion": test_patient_data["tipoAtencion"],
                "observaciones": test_patient_data["observaciones"]
            }
            
            structure_valid = all(
                retrieved_patient.get(key) == expected_structure[key] 
                for key in expected_structure.keys()
            )
            
            if structure_valid:
                print("✓ Document structure is valid")
                print("✓ _id is now the numeroCedula as required")
            else:
                print("✗ Document structure validation failed")
                
        else:
            print("✗ Patient not found after insertion")
            
        # Cleanup
        await db.pacientes.delete_one({"_id": test_patient_data["numeroCedula"]})
        print("✓ Test cleanup completed")
        
    except Exception as e:
        print(f"✗ Error during test: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_patient_structure())
