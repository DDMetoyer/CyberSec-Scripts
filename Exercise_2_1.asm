

    global  _main
    extern  _printf
    extern  _ExitProcess@4

section .bss
name:      resb 100
position1: resz 1
position2: resz 1
position3: resz 1


section .data
jolly:  db "For he's is a jolly good fellow!", 0ah, 0
deny:   db 'Which nobody can deny!', 0ah, 0

section .text
    mov ecx, 3            ; Set loop counter to 3
loop_start:
    push dword jolly       ; Push the string to stack for printf
    call _printf           ; Print "For he's a jolly good fellow!"
    add esp, 4             ; Clean up the stack
    dec ecx                ; Decrement counter
    jnz loop_start         ; Jump if counter not zero
_main:
       
        push   jolly         ;  push the jolly string and call printf
        call   _printf
		add    esp, 4        ;  restore the stack pointer

        push   deny          ;  push the deny string and call printf
        call   _printf
		add    esp, 4        ;  restore the stack pointer

        xor     ecx,ecx      ;  set the exit code to 0

        call    _ExitProcess@4