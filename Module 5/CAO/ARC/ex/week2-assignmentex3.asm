.begin
.org 0
	sethi arr1, %r1
	srl %r1, 10, %r1
	and %r0, %r10, %r10
loop:	ld [%r1], %r2
	orcc %r2, %r0, %r0
	be finished
	addcc %r2, -2, %r0
	be increment
	ba next
increment: inc %r10
next:	add %r1, 4, %r1
	ba loop
finished: halt
	

.org 200
arr1:	5,4,3,6,2,5,4,2,1,2,2,3,4,5,1,2,3,54,0

.end
