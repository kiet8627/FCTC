
#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

;; put your code below

(define (sequence low high stride)
  (if (> low high)
      null
      (cons low (sequence (+ low stride) high stride))))

(define (string-append-map xs suffix)
  (map (lambda (s) (string-append s suffix)) xs))

(define (list-nth-mod xs n)
  (cond [(< n 0) (error "list-nth-mod: negative number")]
        [(null? xs) (error "list-nth-mod: empty list")]
        [#t (list-ref xs (remainder n (length xs)))]))

(define (stream-for-n-steps s n)
  (if (= n 0)
      null
      (let ([next (s)])
            (cons (car next) (stream-for-n-steps (cdr next) (- n 1))))))

(define funny-number-stream 
  (letrec ([f (lambda (n) (cons (if (= (remainder n 5) 0) (- n) n)
                                (lambda () (f (+ n 1)))))])
    (lambda () (f 1))))

(define (dan-then-dog)
  (cons "dan.jpg"
        (lambda () (cons "dog.jpg" dan-then-dog))))

(define (stream-add-zero s)
  (lambda () (cons (cons 0 (car (s))) (stream-add-zero (cdr (s))))))

(define (cycle-lists xs ys)
  (letrec ([get-firsts (lambda (pos)
                         (cons (cons (list-nth-mod xs pos) (list-nth-mod ys pos))
                               (lambda () (get-firsts (+ pos 1)))))])
    (lambda () (get-firsts 0))))

(define (vector-assoc v vec)
  (letrec ([find-value (lambda (pos)
                         (if (= pos (vector-length vec))
                             #f
                             (let ([value (vector-ref vec pos)])
                               (if (or (not (pair? value))
                                       (not (equal? (car value) v)))
                                   (find-value (+ pos 1))
                                   value))))])
    (find-value 0)))

(define (cached-assoc xs n)
  (letrec ([cache (make-vector n)]
           [index 0])
    (lambda (v)
      (let ([cached-value (vector-assoc v cache)])
        (if cached-value
            cached-value
            (let ([value (assoc v xs)])
              (if value
                  (begin (vector-set! cache (remainder index n) value)
                         (set! index (+ index 1))
                         value)
                  #f)))))))
