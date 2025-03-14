global  _main
extern  _printf
extern  _scanf
extern  _ExitProcess@4

section .data
prompt:         db 'Enter a number: ', 0
format_in:      db '%d', 0
output:         db 'The value of %d! is %d.', 0Ah, 0
error_message:  db 'Error: Factorial is not defined for negative numbers.', 0Ah, 0

section .bss
number:     resd 1       ; Reserve 4 bytes for the number entered by the user
result:     resd 1       ; Reserve 4 bytes for the factorial result
counter:    resd 1       ; Reserve 4 bytes for the loop counter

section .text
_main:
    ; Prompt the user to enter a number
    push    dword prompt
    call    _printf
    add     esp, 4

    ; Read the number from the user
    lea     eax, [number]
    push    eax
    push    dword format_in
    call    _scanf
    add     esp, 8

    ; Move the number to EAX and check if it's negative
    mov     eax, [number]
    cmp     eax, 0
    jl      negative_input   ; If number < 0, jump to negative_input

    ; For number <= 1, factorial is 1
    cmp     eax, 1
    jle     factorial_done   ; If number <= 1, skip calculation

    ; Initialize result to number
    mov     [result], eax

    ; Initialize counter to number - 1
    mov     ebx, eax
    dec     ebx
    mov     [counter], ebx

    ; Loop to calculate factorial
factorial_loop:
    ; Multiply result *= counter
    mov     eax, [result]
    mov     ebx, [counter]
    imul    eax, ebx         ; EAX = EAX * EBX
    mov     [result], eax

    ; Decrement counter
    dec     dword [counter]
    cmp     dword [counter], 1
    jge     factorial_loop   ; While counter >= 1, loop again

factorial_done:
    ; For number <= 1, set result to 1
    cmp     dword [number], 1
    jg      skip_set_result  ; If number > 1, skip setting result to 1
    mov     dword [result], 1

skip_set_result:
    ; Print the result
    push    dword [result]       ; Push factorial result
    push    dword [number]       ; Push original number
    push    dword output         ; Push output format string
    call    _printf
    add     esp, 12              ; Clean up the stack

    ; Exit the program
    push    0
    call    _ExitProcess@4

negative_input:
    ; Print error message
    push    dword error_message
    call    _printf
    add     esp, 4               ; Clean up the stack

    ; Exit the program
    push    0
    call    _ExitProcess@4
