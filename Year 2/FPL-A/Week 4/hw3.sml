(* Coursera Programming Languages, Homework 3, Provided Code *)

exception NoAnswer

datatype pattern = Wildcard
		 | Variable of string
		 | UnitP
		 | ConstP of int
		 | TupleP of pattern list
		 | ConstructorP of string * pattern

datatype valu = Const of int
	      | Unit
	      | Tuple of valu list
	      | Constructor of string * valu

fun g f1 f2 p =
    let 
	val r = g f1 f2 
    in
	case p of
	    Wildcard          => f1 ()
	  | Variable x        => f2 x
	  | TupleP ps         => List.foldl (fn (p,i) => (r p) + i) 0 ps
	  | ConstructorP(_,p) => r p
	  | _                 => 0
    end

(**** for the challenge problem only ****)

datatype typ = Anything
	     | UnitT
	     | IntT
	     | TupleT of typ list
	     | Datatype of string

(**** you can put all your code here ****)

val only_capitals = List.filter(fn s => (Char.isUpper o String.sub) (s, 0))

val longest_string1 =
    List.foldl (fn (s, acc) => if (String.size s) > (String.size acc)
			       then s
			       else acc) ""

val longest_string2 =
    List.foldl (fn (s, acc) => if (String.size s) >= (String.size acc)
			       then s
			       else acc) ""

fun longest_string_helper f =
    List.foldl (fn (s, acc) => if f (String.size s, String.size acc)
				then s
				else acc) ""

val longest_string3 = longest_string_helper (fn (a, b) => a > b)
val longest_string4 = longest_string_helper (fn (a, b) => a >= b)

val longest_capitalized = longest_string1 o only_capitals

val rev_string = implode o rev o explode

(* _________________________________________________________________________________________ *)

fun first_answer f l =
    case l of
	[] => raise NoAnswer
      | x :: xs => case f x of
		       SOME v => v
		     | NONE => first_answer f xs

fun all_answers f l =
    let
	fun all_answers_helper l' acc =
	    case (l', acc) of
		([], _) => acc
	      | (x :: xs, SOME v) => (case f x of
					  NONE => NONE
					| SOME v' => all_answers_helper xs (SOME (v @ v')))
	      | _ => NONE
    in
	all_answers_helper l (SOME [])
    end

(* _________________________________________________________________________________________ *)

val count_wildcards = g (fn _ => 1) (fn _ => 0)

val count_wild_and_variable_lengths = g (fn _ => 1) String.size

fun count_some_var (str, p) = g (fn _ => 0) (fn x => if String.isSubstring str x
						     then 1 else 0) p

fun check_pat p =
    let
	fun filterString pat acc = case pat of
				       Variable x => x :: acc
				     | ConstructorP (_, p) => filterString p acc
				     | TupleP ps =>
				       List.foldl
					   (fn (p, acc) => (filterString p []) @ acc) [] ps
				     | _ => []
    in
	let
	    val strList = filterString p []
	    fun checkDuplicate remList = 
		case remList of
		    [] => true
		  | x :: xs => if List.exists (fn item => item = x) xs
			       then false
			       else checkDuplicate xs
	in
	    checkDuplicate strList
	end
    end

fun match (v, p) =
    case p of
	Wildcard => SOME []
      | UnitP => (case v of Unit => SOME []
			  | _ => NONE)
      | Variable str => SOME [(str, v)]
      | ConstP i => (case v of Const j => if i = j then SOME [] else NONE
			     | _ => NONE)
      | TupleP plst => (case v of
			    Tuple vlst => if List.length plst = List.length vlst
					  then all_answers match (ListPair.zip (vlst, plst))
					  else NONE
			  | _ => NONE)
      | ConstructorP (str, pt) => (case v of
				       Constructor (vstr, vval) => if str = vstr
								   then match (vval, pt)
								   else NONE
				     | _ => NONE)

fun first_match v plst =
    SOME (first_answer (fn p => match (v, p)) plst)
    handle NoAnswer => NONE
