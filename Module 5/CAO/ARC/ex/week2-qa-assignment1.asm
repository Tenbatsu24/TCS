.begin
.org 0

	sethi	arr1, %r1
	srl	%r1, 10, %r1
loop:	ld 	[%r1], %r2
	orcc 	%r2, %r0, %r0
	be finished
	andcc 	%r2, 1, %r0
	be next
	call twoc
	add 	%r2, 1, %r2
	st 	%r2, %r1
	ld [%r1], %r31
next:	add %r1, 4, %r1
	ba loop
finished:	halt

twoc:	orncc %r0, %r2, %r2
	jmpl %r15+4, %r0
arr1:	-1, 0
.end
