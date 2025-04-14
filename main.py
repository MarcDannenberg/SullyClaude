# main.py
from fastapi import FastAPI, File, UploadFile, Form, Query, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Dict, Optional, Any, Union
import os
import json
import random
import datetime
from pathlib import Path

# Import modules
from conversation_engine import ConversationEngine
from reasoning import SymbolicReasoningNode
from Codex import SullyCodex
from math_translator import SymbolicMathTranslator
from memory import SullySearchMemory
from dream import DreamCore
from sully import Sully
from fusion import SymbolFusionEngine
from paradox import ParadoxLibrary

# Initialize the Codex
codex = SullyCodex()

# Initialize the math translator
translator = SymbolicMathTranslator()

# Initialize the memory system
memory_system = SullySearchMemory()

# Initialize the reasoning node
reasoning_node = SymbolicReasoningNode(codex, translator, memory_system)

# Initialize the conversation engine
conversation_engine = ConversationEngine(reasoning_node, memory_system, codex)

# Initialize the dream core
dream_core = DreamCore()

# Initialize the Sully system
sully_system = Sully()

# Initialize the symbol fusion engine
fusion_engine = SymbolFusionEngine()

# Initialize the paradox library
paradox_library = ParadoxLibrary()

# Create FastAPI app
app = FastAPI(
    title="Sully Resonance Core API",
    description="API for Sully, a sophisticated cognitive system with recursive, paradox-aware capabilities",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request/response models
class ChatRequest(BaseModel):
    message: str
    mode: str = "emergent"
    continue_conversation: bool = True

class RememberRequest(BaseModel):
    content: str
    source: str
    concepts: Optional[List[str]] = None
    importance: float = 0.5

class EvaluateRequest(BaseModel):
    text: str

class FuseRequest(BaseModel):
    inputs: List[str]

# API Routes
@app.post("/api/sully/chat")
async def chat(request: ChatRequest):
    """Engage with Sully using different cognitive modes"""
    response = conversation_engine.process_message(
        request.message,
        tone=request.mode,
        continue_conversation=request.continue_conversation
    )
    
    return {
        "response": response,
        "topics": conversation_engine.current_topics,
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.post("/api/sully/remember")
async def remember(request: RememberRequest):
    memory_index = memory_system.store_experience(
        content=request.content,
        source=request.source,
        concepts=request.concepts,
        importance=request.importance
    )
    return {
        "status": "stored",
        "index": memory_index,
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.get("/api/sully/dream")
async def dream(
    seed: str = Query(...)
):
    dream_result = sully_system.dream(seed=seed)
    
    return {
        "dream": dream_result,
        "seed": seed,
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.post("/api/sully/evaluate")
async def evaluate(request: EvaluateRequest):
    result = sully_system.evaluate_claim(request.text)
    return {
        "claim": request.text,
        "evaluation": result.get("evaluation") if isinstance(result, dict) else result,
        "confidence": result.get("confidence", 1.0) if isinstance(result, dict) else 1.0,
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.get("/api/sully/translate")
async def translate(phrase: str = Query(...)):
    translation = sully_system.translate_math(phrase)
    return {
        "original": phrase,
        "translation": translation
    }

@app.post("/api/sully/fuse")
async def fuse(request: FuseRequest):
    inputs = request.inputs

    # Use the SymbolFusionEngine to perform the fusion using the basic fuse function
    fusion_result = sully_system.fuse(*inputs)

    # Return the full response that includes all information from fuse_with_options
    if isinstance(fusion_result, dict):
        return {
            "inputs": fusion_result["inputs"],
            "style": fusion_result["style"],
            "formal_representation": fusion_result["formal_representation"],
            "result": fusion_result["result"],
            "formatted_result": fusion_result["formatted_result"],
            "comment": fusion_result["comment"],
            "timestamp": datetime.datetime.now().isoformat()
        }

    # In case the result is a string (fusion failed or not enough symbols)
    return {
        "fusion_result": fusion_result,
        "timestamp": datetime.datetime.now().isoformat()
    }

@app.get("/api/sully/paradox")
async def paradox(topic: str = Query(...)):
    # Retrieve the paradox using the get function
    paradox_result = sully_system.reveal_paradox(topic)
    
    # Include the perspective and topic in the response
    response = {
        "topic": topic,
        "paradox": paradox_result
    }

    # If the paradox has additional information (e.g., type, resolution strategies), include it
    if 'type' in paradox_result:
        response['paradox_type'] = paradox_result['type']
        response['paradox_description'] = paradox_result['description']
        response['resolution_strategies'] = paradox_result.get('resolution_strategies', [])

    # If a reframed paradox exists, include it as well
    if 'reframed' in paradox_result:
        response['reframed'] = paradox_result['reframed']
    
    # Add any notes (like "This paradox was dynamically generated...")
    if 'note' in paradox_result:
        response['note'] = paradox_result['note']
    
    # Return the full response
    return response

@app.post("/api/sully/ingest")
async def ingest(file: UploadFile = File(...)):
    os.makedirs("temp", exist_ok=True)
    
    file_location = f"temp/{file.filename}"
    
    with open(file_location, "wb") as f:
        f.write(await file.read())
    
    result = sully_system.ingest_document(file_location)
    
    os.remove(file_location)
    
    return {"status": "ingested", "summary": result}

@app.post("/api/sully/ingest_folder")
async def ingest_folder(files: List[UploadFile] = File(...)):
    os.makedirs("temp", exist_ok=True)
    results = []
    
    # Process each uploaded file
    for file in files:
        file_location = f"temp/{file.filename}"
        
        with open(file_location, "wb") as f:
            f.write(await file.read())
        
        result = sully_system.ingest_document(file_location)
        
        os.remove(file_location)
        
        results.append({"file": file.filename, "status": "ingested", "summary": result})
    
    return {"status": "batch_ingested", "results": results}



if __name__ == "__main__":
    # Note: When running as a script, use:
    # uvicorn sully_api:app --reload
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)