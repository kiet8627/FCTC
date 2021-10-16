(* Dan Grossman, Coursera PL, HW2 Provided Code *)

(* if you use this function to compare two strings (returns true if the same
   string), then you avoid several of the functions in problem 1 having
   polymorphic types that may be confusing *)
fun same_string(s1 : string, s2 : string) =
    s1 = s2

(* put your solutions for problem 1 here *)
fun all_except_option(s, xs) =
    case xs of
	[] => NONE
      | x :: xs' => if same_string(s, x)
		    then SOME xs'
		    else case all_except_option(s, xs') of
			     NONE => NONE
			   | SOME l => SOME (x :: l)

fun get_substitutions1(xs, s) =
    case xs of
	[] => []
      | x :: xs' => case all_except_option(s, x) of
			NONE => get_substitutions1(xs', s)
		      | SOME l => l @ get_substitutions1(xs', s)

fun get_substitutions2(xs, s) =
    let
	fun aux(xs, s, acc) =
	    case xs of
		[] => acc
	      | x :: xs' => case all_except_option(s, x) of
				NONE => aux(xs', s, acc)
			      | SOME l => aux(xs', s, l @ acc)
    in
	aux(xs, s, [])
    end

fun similar_names(substitutions, name) =
    let
	val {first = x1, middle = x2, last = x3} = name
	fun get_names xs =
	    case xs of
		[] => []
	      | x :: xs' => {first = x, middle = x2, last = x3} :: (get_names(xs'))
    in
	name::get_names(get_substitutions2(substitutions, x1))
    end

(* you may assume that Num is always used with values 2, 3, ..., 10
   though it will not really come up *)
datatype suit = Clubs | Diamonds | Hearts | Spades
datatype rank = Jack | Queen | King | Ace | Num of int 
type card = suit * rank

datatype color = Red | Black
datatype move = Discard of card | Draw 

exception IllegalMove

(* put your solutions for problem 2 here *)
fun card_color(s, _) =
    case s of
	Spades => Black
      | Clubs => Black
      | _ => Red

fun card_value(_, r) =
    case r of
	Num n => n
      | Ace => 11
      | _ => 10

fun remove_card(cs, c, e) =
    case cs of
	[] => raise e
      | h :: t => if h = c
		  then t
		  else h :: remove_card(t, c, e)

fun all_same_color(cs) =
    case cs of
	[] => true
      | h :: t => case t of
		      [] => true
		    | h' :: t' => (card_color h = card_color h') andalso all_same_color t

fun sum_cards(cs) =
    let
	fun aux(cs, acc) =
	    case cs of
		[] => acc
	      | h :: t => aux(t, acc + card_value(h))
    in
	aux(cs, 0)
    end

fun score(held_cards, goal) =
    let
	val sum = sum_cards held_cards
	fun preliminary_score(sum, goal) =
	    if sum > goal
	    then 3 * (sum - goal)
	    else goal - sum
    in
	if all_same_color held_cards
	then preliminary_score(sum, goal) div 2
	else preliminary_score(sum, goal)
    end

fun officiate(card_list, moves, goal) =
    let
	fun play(card_list, card_helds, moves) =
	    case moves of
		[] => card_helds
	      | h :: t => case h of
			      Discard c => play(card_list, remove_card(card_helds, c, IllegalMove), t)
			    | Draw => case card_list of
					  [] => card_helds
					| c :: cs => if sum_cards (c :: card_helds) > goal
						     then c :: card_helds
						     else play(cs, c :: card_helds, t)
    in
	score(play(card_list, [], moves), goal)
    end
