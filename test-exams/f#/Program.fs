// Questions 1 - 6 Multi-paradigm programming in F#

// Question 1

//1a

let sqrOnlyFirst ls =
    match ls with
    | [] -> 0
    | hd :: _ -> hd * hd

let res1 = sqrOnlyFirst [2;4;6]
let res2 = sqrOnlyFirst []

// 1b

let rec stringToList(str: string) = 
    match str with
    | "" -> []
    | _ -> str.[0] :: stringToList(str[1..])

let jebo = stringToList("kokot")

// Question 2

// 2a

// record type
type Vector = {
    a: int
    b: int
    c: int
    d: int
    e: int
}

let vecLen vector = vector.a + vector.b + vector.c + vector.d + vector.e

let result2a = vecLen({1, 2, 3, 4, 5})

let vecAdd vector1 vector2 = 
    { 
        a = vector1.a  + vector2.a;
        b = vector1.b  + vector2.b;
        c = vector1.c  + vector2.c;
        d = vector1.d  + vector2.d;
        e = vector2.e + vector2.e;
    }

// Question 3
// Recursive functions and variants.

let rec rerun(str: string, sep: string, n: int) = 
    if n > 0
    then str + sep + rerun(str, sep, n-1)
    else ""

let res3 = rerun("kokot dopice", " ", 10)
let res3_ = rerun("kokot dopice", " ", 0)


// 3b 
// tail recursive 
let rerunTail(str: string, sep: string, n: int) = 
    let rec rerunInner(str: string, sep: string, n: int, acc) = 
        if n > 0
        then rerunInner(str, sep, n-1, acc + sep + str)
        else acc
    rerunInner(str, sep, n, "")

let res3b = rerunTail("kokot dopice", " ", 10)

// question 4

// given declarations:

let f1 i j k =
    seq {
         for x in [0 .. i] do
             for y in [0 .. j] do
             if x+y < k then yield (x,y)
    }
let f2 f p sq =
    seq {
         for x in sq do
            if p x then yield f x
    }
let f3 g sq =
    seq {
         for s in sq do
            yield! g s
    }


// 4a
let valueOf = List.ofSeq (f1 2 2 3)
 // [(0, 0); (0, 1); (0, 2); (1, 0); (1, 1); (2, 0)]

// 4b

// let f2alt = 

let function2HumanLanguage func predicate sequence =
    seq {
         for x in sequence do
            if predicate x then yield func x
    }

let f1seq = f1 2 2 3

let f2seq func predicate sequence = 
    sequence
    |> Seq.filter predicate
    |> Seq.map func



// Question 5

type expr = 
    | Const of int
    | BinOpr of expr * string * expr

//5a
// discriminated union
// tuples
// expr
// expression
// to string
// print

let expr1 = Const(1)
let expr2 = BinOpr(Const(1), "+", Const(1))
let expr3 = BinOpr(Const(1), "+", BinOpr(Const(2), "*", Const(3)))

// 5b

let rec toString(ex: expr) =
    match ex with
    | Const(x) -> x.ToString()
    | BinOpr(ex1, opr, ex2) -> toString(ex1) + opr + toString(ex2)

let strExp1 = toString(expr1)
let strExp2 = toString(expr2)
let strExp3 = toString(expr3)

// Question 6

// Recall from the lessons that F# provides the generic MailboxProcessor class as its
// implementation of message passing and the actor model.
// Write an F# agent/actor to add and get products, for instance in an inventory management system. 
// The product can simply consist of a name and quantity.

type Product = {
    name: string
    quantity: int
}
// agent/actor (same thing)
// mailbox

let productAgent: MailboxProcessor<Product> = 
    MailboxProcessor.Start(fun inbox ->
        let rec loop () =
            async {
                let! incoming = inbox.Receive()
                
                printfn "%s %d" incoming.name incoming.quantity 
                printfn "\n"

                return! loop ()
            }

        loop())

let order1 = productAgent.Post({ 
    name = "Picovina" 
    quantity = 69420
    })
    