from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Code(BaseModel):
    text: str

app = FastAPI()

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/interpret/")
async def interpret_code(code: Code):
    interpret_code(get_user_input(code.text))
    return code

def get_user_input(code):
    code_by_line = code.splitlines()
    code_dict = { i :  code_by_line[i] for i in range(0, len(code_by_line)) }
    return code_dict

def exec_function(user_input):

	try:
		compile(user_input, '<stdin>', 'eval')
	except SyntaxError:
		return exec
	return eval


def exec_user_input(i, user_input, user_globals):

	user_globals = user_globals.copy()
	try:
		retval = exec_function(user_input)(
			user_input, user_globals
		)
	except Exception as e:
		print('%s: %s on line %i' % (e.__class__.__name__, e, i))
	else:
		if retval is not None:
			print('Out [%d]: %s' % (i, retval))
	return user_globals


def selected_user_globals(user_globals):
	return (
		(key, user_globals[key])
		for key in sorted(user_globals)
		if not key.startswith('__') or not key.endswith('__')
	)


def save_user_globals(user_globals, path='user_globals.txt'):
	for key, val in selected_user_globals(user_globals):
			print(key, val)


def interpret_code(code_dict):
	user_globals = {}
	save_user_globals(user_globals)
	for i, user_input in code_dict.items():
		user_globals = exec_user_input(
			i, user_input, user_globals
		)
		save_user_globals(user_globals)