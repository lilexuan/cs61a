;; Extra Scheme Questions ;;


(define lst
  (list 
    (cons 1 nil)
    2
    (cons 3 (cons 4 nil))
    5
  )
)

(define (composed f g)
  (lambda (x)
    (f (g x))
  )
)

(define (remove item lst)
  'YOUR-CODE-HERE
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (no-repeats s)
  'YOUR-CODE-HERE
)

(define (substitute s old new)
  'YOUR-CODE-HERE
)

(define (sub-all s olds news)
  'YOUR-CODE-HERE
)