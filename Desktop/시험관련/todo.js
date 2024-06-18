function createTodo() {
    const todoList = document.querySelector('#todoList');
    const newLi = document.createElement('li');
    const newCheckbox = document.createElement('input');
    newCheckbox.type = 'checkbox';
    const indexSpan = document.createElement('span'); // 숫자를 표시할 span
    const newSpan = document.createElement('span'); // 할 일 텍스트를 표시할 span
    const todoInput = document.querySelector('#todoInput');

    // 할 일 목록의 현재 길이를 기반으로 인덱스 번호 설정
    indexSpan.textContent = todoList.children.length + 1 + ". ";
    indexSpan.style.fontWeight = '500'; // 번호에 대한 스타일 설정

    newCheckbox.addEventListener('change', () => {
        newLi.classList.toggle('complete');
    });

    // li 요소 내에 체크박스, 숫자 span, 텍스트 span 순으로 추가
    newLi.appendChild(newCheckbox);
    newLi.appendChild(indexSpan);
    newLi.appendChild(newSpan);
    newSpan.textContent = todoInput.value;
    todoList.appendChild(newLi);
    todoInput.value = ''; // 입력 필드 초기화
}
