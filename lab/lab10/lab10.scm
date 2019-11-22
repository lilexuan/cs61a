; ; Scheme ;;
(define (repeatedly-cube n x)
  (if (zero? n)
      x
      (let ((n (- n 1))
            (y (repeatedly-cube (- n 1) x))
           )
        (* y y y)
      )
  )
)
