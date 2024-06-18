let currentInput = '';
let resultDisplay = document.getElementById('resultDisplay');

function inputDigit(digit) {
    currentInput += digit;
    resultDisplay.textContent = currentInput;
}

function inputOperator(operator) {
    if (currentInput.length && !isNaN(currentInput[currentInput.length - 1])) {
        currentInput += operator;
        resultDisplay.textContent = currentInput;
    }
}

function calculateResult() {
    try {
        const result = eval(currentInput);
        resultDisplay.textContent = result;
        currentInput = result.toString();
    } catch (error) {
        resultDisplay.textContent = 'Error';
        currentInput = '';
    }
}

function clearDisplay() {
    currentInput = '';
    resultDisplay.textContent = '0';
}

function inputPercent() {
    if (currentInput.length && !isNaN(currentInput)) {
        currentInput = (parseFloat(currentInput) / 100).toString();
        resultDisplay.textContent = currentInput;
    }
}

function toggleSign() {
    if (currentInput.startsWith('-')) {
        currentInput = currentInput.slice(1);
    } else {
        currentInput = '-' + currentInput;
    }
    resultDisplay.textContent = currentInput;
}

function inputDecimal() {
    if (!currentInput.includes('.')) {
        currentInput += '.';
        resultDisplay.textContent = currentInput;
    }
}

function inputParentheses() {
    if (currentInput.includes('(') && !currentInput.includes(')')) {
        currentInput += ')';
    } else {
        currentInput += '(';
    }
    resultDisplay.textContent = currentInput;
}
