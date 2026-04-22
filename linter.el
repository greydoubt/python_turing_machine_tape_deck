; lambda function definition
(defpat parsing ( ['function nm parameters $ code] )
   (setq code (maplist 'parsing code false))   
   (nconcn (list 'defun (atom nm) (parsing parameters)) code))

(setq sz (getOutputSize))
(setq lst (list))
;
(loop i 
   (irange sz)
   (setq r (json_parse (getOutputDataValue i)))
   (loop u r
      (check (in_it u "bad_nlu")
         (setq a (at u "bad_nlu"))
         (maybe (setq a (json_parse a)) (set@ u "bad_nlu" a) (λ (e_) (println "Erreur:" i)))))(push lst r))

