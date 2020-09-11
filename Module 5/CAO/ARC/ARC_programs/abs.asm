.begin
.org 0
	ld[x], %r1
	subcc %r0, %r1, %r1
	bneg over
	st %r1, [x]
over:	halt
x:	-10
.end
