;; Scheme ;;

(define (over-or-under x y)
  (cond
    ((< x y) -1)
    ((> x y) 1)
    (else 0))
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

; recursive condition: if node_now meets f, then cons node_now and the rest(process in recursive
;                      if node_now dont't meets f , then return the rest(process recursively)
; recursive ending: if node_now is null, return ()
(define (filter-lst f lst)
  (cond 
    ((null? lst) ())
    ((f (car lst)) (cons (car lst) (filter-lst f (cdr lst))))
    (else (filter-lst f (cdr lst)))
  )
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

(define (make-adder num)
  'YOUR-CODE-HERE
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13