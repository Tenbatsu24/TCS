! This program adds two numbers
	.begin 
	.org 0
	ld	[x], %r1	! Load x into %r1
	ld	[y], %r2	! Load y into %r2
	addcc	%r1, %r2, %r3	! %r3 <- %r1 + %r2
	st	%r3, [z]	! store %r3 into z
	halt
x:	15
y:	9
z:	0
	.end
