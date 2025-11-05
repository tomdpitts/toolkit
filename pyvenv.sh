pyvenv() {
  if [ -z "$1" ]; then
    echo "Usage: pyvenv <directory-name>"
    return 1
  fi

  VENV_DIR="$1"
  PYTHON_BIN=$(which python3)

  if [ -z "$PYTHON_BIN" ]; then
    echo "Python3 is not installed. Please install it first."
    return 1
  fi

  if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment in ./$VENV_DIR ..."
    $PYTHON_BIN -m venv "$VENV_DIR"
  else
    echo "Virtual environment directory ./$VENV_DIR already exists."
  fi

  echo "Activating virtual environment..."
  source "$VENV_DIR/bin/activate"
}