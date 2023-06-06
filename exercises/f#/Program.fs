    // Starting up a new f# project:

// Open VS Code Terminal or your preferred command-line interface.
// Navigate to the directory where you want to create your project.
// Run the following command: dotnet new console -lang F# -n YourProjectName
// This command will create a new F# console project with the name YourProjectName. The project will be created within a new directory also named YourProjectName.

// So if you wanted to create a project called AwesomeFSharpProject, you would run: dotnet new console -lang F# -n AwesomeFSharpProject.

// You can then open the newly created project in VS Code by navigating into the project directory (cd YourProjectName) and typing code . to launch VS Code.

// Remember to replace YourProjectName with the actual name you want for your project.

// For more information see https://aka.ms/fsharp-console-apps
printfn "Hello from F#"

// 2.1 

let vowelToUpper c: char =
    match c with
    | 'a' -> 'A'
    | 'e' -> 'E'
    | 'i' -> 'I'
    | 'o' -> 'O'
    | 'u' -> 'U'
    | _ -> c

let result2_1 = vowelToUpper('i')


// 2.2 

let rec length(list): int = 
    match list with
    | [] -> 0
    | _ :: tail  -> 1 + length(tail)

let result2_2 = length ['a'; 'b'; 'c']


// 2.3

let rec takeSome(n: int, list) = 
    match (n, list) with
    | 0, _ | _, [] -> []
    | _, head :: tail when n > 0 -> head :: takeSome(n-1, tail)
    | _ -> failwith("Invalid input")

let result2_3  = takeSome(2, ['1'; '2' ; '3';])


// 2.4

let rec pclFold(func, acc, list) = 
    match list with
    | [] -> acc
    | head :: tail -> pclFold(func, func(acc, head), tail)

let result2_4 = pclFold((fun(acc, head) -> acc + head), 0, [1;2;5])

    
// 2.5 

let rec pclFoldBack(func, acc, list) = 
    match list with
    | [] -> acc
    | head :: tail -> func(head, pclFoldBack(func, acc, tail))


let resultFold = pclFold((fun(acc, head) -> acc - head), 0, [1;2;3]) // resultFold will be -6
let resultFoldBack = pclFoldBack((fun(head, acc) -> head - acc), 0, [1;2;3]) // resultFoldBack will be 2

// 2.6

let rec pclIncList(list) =
    match list with
    | [] -> []
    | head :: tail -> head+1 :: pclIncList(tail)

let result2_6 = pclIncList([1;2;3])


// 2.7 
let rec pclMap(func, list) = 
    match list with
    | [] -> []
    | head :: tail -> func(head) :: pclIncList(tail)

// 2.7 b
let result2_7 = pclMap((fun(head) -> head+1), [1;2;3])


// 2.8
let rec pclFilter(predicate, list) = 
    match list with 
    | [] -> []
    | head::tail when predicate(head) -> head :: pclFilter(predicate, tail)
    | _::tail -> pclFilter(predicate, tail)

let result2_8 = pclFilter((fun(head)-> head % 2 = 0), [1;2;3;4;5;6;7;8;9])

// Higher-order functions, partial function application, closures

// 3.1
let rec countNumOfVowels(input: string): int * int * int * int * int =
    let initialAccumulator = (0, 0, 0, 0, 0)

    input
    |> List.ofSeq
    |> List.fold (fun (aCount, eCount, iCount, oCount, uCount) c -> 
        match System.Char.ToLower(c) with
        | 'a' -> (aCount+1, eCount, iCount, oCount, uCount)
        | 'e' -> (aCount, eCount+1, iCount, oCount, uCount)
        | 'i' -> (aCount, eCount, iCount+1, oCount, uCount)
        | 'o' -> (aCount, eCount, iCount, oCount+1, uCount)
        | 'u' -> (aCount, eCount, iCount, oCount, uCount+1)
        | _   -> (aCount, eCount, iCount, oCount, uCount)
    ) initialAccumulator

let result3_1 = countNumOfVowels "Higher-order functions can take and return functions of any order"


// 3.2


let isPrime(num:int) =
    let dividors = [2 .. (num/2)]
    let filtered = List.filter (fun(dividor) -> num % dividor = 0) dividors
    if List.isEmpty(filtered) then true 
    else false


let primesUpTo(num) = 
    let upTo = [2 .. num]
    List.filter (fun number -> isPrime number) upTo

let primes = primesUpTo(10)



// 3.3

let pclFib n = 
    let rec fibInner(n, nCurrent, prev, current) =
        if nCurrent <= n 
        then fibInner(n, nCurrent+1, current, prev+current)
        else current

    match n with
    | 0 -> 0
    | _ -> fibInner(n, 2, 0, 1)

let result3_3 = pclFib(8)


// 3.4

let doubleNum x = x*2
let sqrNum x = x*x
let pclQuad x = doubleNum(doubleNum(x))
let pclFourth x = sqrNum(sqrNum(x))

let testValues = [1; 2; 3; 4; 5]

// Apply each function to each test value
let doubleResults = List.map doubleNum testValues
let sqrResults = List.map sqrNum testValues
let quadResults = List.map pclQuad testValues
let fourthResults = List.map pclFourth testValues


// 4.1

type Rectangle = {
    Width: float
    Height: float
}

type RightTriangle = {
    Base: float
    Height: float
}

let myRectangle = { Width = 10.0; Height = 20.0 }
let myTriangle = { Base = 5.0; Height = 10.0 }

type PclShape =
    | Rectangle of Rectangle
    | RightTriangle of RightTriangle
    
let pclArea(shape: PclShape) =
    match shape with
    | Rectangle r -> r.Width * r.Height
    | RightTriangle t -> t.Base * t.Height * 0.5

let pclPerimeter(r: Rectangle) = (r.Height * 2.0) + (r.Width * 2.0)


// 5.1 is - Redefine the pclArea function (defined in Exercise 4.1) to use the new data type (PclShapeR 4.1e). Call the new function pclAreaRec.
// 4.1e - Redefine the PclShape to use records instead of tuples (PclShapeR).
// so... I made 5.1 in 4.1 already



// 5.2 Redefine the fibonacci function (defined in Exercise 3.3) as a tail recursive function
// already done in pclFib
let fib = pclFib(10)

// 5.3 Redefine the accumulator based factorial function from today’s lesson to use continuations.

let accFactorial(x) =
    if x < 0 then failwith "Non natural number arg"
    // Keep track of both x and accumulator value (acc)
    let rec tailRecursiveFactorial (x, acc) =
        if x <= 1 
        then acc
        else tailRecursiveFactorial((x-1), (acc * x))
        
    tailRecursiveFactorial(x, 1)

let contFactorial(x: int) = 
    if x < 0 then failwith "Non natural number arg"
    let rec factorialAux(n, cont) =
        if n <= 1 
        then cont 1
        else factorialAux(n-1, (fun result -> cont(result * n)))

    factorialAux(x, (fun x -> x))

let contResult6 = contFactorial 5  // expected: 120
printfn "Factorial of 5 is %d" contResult6x


// from presentation
let printListRev(lst) =
    let rec printListRevTR (lst, cont )=
        match lst with
        // For an empty list, execute the continuation
        | [] -> cont()
        // for other lists, print the current node as part of the cont 
        | head :: tail -> printListRevTR(tail, (fun () -> printf "%A " head; cont()))

    printListRevTR(lst, (fun () -> printfn "Done!"))


printListRev testValues


// tail recursive sum

let sum list =
    let rec sumWithCont list cont =
        match list with
        | [] -> cont 0
        | head :: tail -> sumWithCont tail (fun result -> cont (head + result))
    sumWithCont list (fun x -> x)


// 6a 6.1
// Declare a type IntegerTree representing a tree of integers and define a recursive function sumIntegerTree that sums all the values in the tree. 
// Test your solution with a couple of inputs.


type Node = {
    value: int
    children: List<Node>
}

let sumIntegerTree(tree: Node) = 

    let rec traverseNode(innerTree,acc) =
        match innerTree with
        | {value = v; children = []} -> v + acc
        | {value = v; children = c} -> 
            let rec traverseChildren(children: List<Node>) = 
                match children with 
                | [] -> 0
                | head :: tail -> traverseNode(head, acc) + traverseChildren(tail) // traversing the first child, and then calling to traverse all other children    
                
            v + traverseChildren(c) // if node has children, return the value + values from all children

    traverseNode(tree, 0)

// the same with fold

// let sumIntegerTree(tree: Node) = 

//     let rec traverseNode(acc, nodes: List<Node>) =
//         List.fold (
//             fun acc {value = v; children = c} ->
//                 let acc = acc + v
//                 traverseNode(acc,c)
//         ) acc nodes
        
//     traverseNode(0, [tree])

let tree1 = {
    value = 5; children = [
        {value =  3; children = []};
        {value =  2; children = [
            {value = 1; children = []}
        ]};
        ]
    }

let tree2 = {
    value = 7; children =[
        {value = 4; children = [
            {value = 3; children = []}
        ]};
        {value = 2; children = []};
        {value = 1; children = []}
    ]
}

let tree3 = { value = 10; children = [] }

// with discriminated union:

type Node = 
    | Node of int * List<Node>

let rec sumIntegerTree (node: Node) : int =
    match node with
    | Node(value, children) ->
        let childSum = List.fold (fun acc childNode -> acc + sumIntegerTree childNode) 0 children
        value + childSum


// let tree1 = Node(5, [Node(3, []); Node(2, [Node(1, [])])])
// let tree2 = Node(7, [Node(4, [Node(3, [])]); Node(2, []); Node(1, [])])
// let tree3 = Node(10, [])

// printfn "Sum of tree1: %i" (sumIntegerTree tree1)  // Expected output: 11
// printfn "Sum of tree2: %i" (sumIntegerTree tree2)  // Expected output: 17
// printfn "Sum of tree3: %i" (sumIntegerTree tree3)  // Expected output: 10


// 6a.2 6.2
// We can use tuples as well as records to return a pair of numbers. 
// For instance, we can count and return the number of words and letters in a given string in a tuple as follows:

let countWordNLetter (str:string) =
    let wordCount = str.Split [|' '|]
    let letterCount = wordCount |> Array.sumBy (fun w -> w.Length)
    (wordCount.Length, letterCount)
           
// test it
countWordNLetter "be happy everything is gonna be okay"

// Convert countWordnLetter function above to use records instead of tuples.

type WordNLetter = {
    words: int
    letters: int
}

let countWordNLetterRec(str: string) = 
    let wordCount = str.Split [|' '|]
    let letterCount = wordCount |> Array.sumBy (fun w -> w.Length)
    {words = wordCount.Length; letters = letterCount}


// Exercise 7 – Leap Year

// Details about the functions:
// This exercise involves calculating with dates: in particular, it involves determining the era-day of a given date, and conversely the date of a given era-day. 
// The era-day of a date d is the number of days between 1 January 1 and d. For example, the era-day of 1 January 1 is 1, the era-day of 31 December 1000 is 365242, and the era-day of 12 March 1999 is 729825.

// A. A year y is a leap-year iff y is divisible by 400 or if it is divisible by 4 and not divisible by 100.
// Define a function isLeap : int -> bool that takes a year y and tells us if y is a leap-year. 
// For example, 2000 and 2020 are both leap-years; 1900 and 2023 are both not leap-years. 


// Translating dates to era-days
// B. The era-day of the last day of year y is 365*y plus 1 for each leap-year between 1 and y. We can use the principle of inclusion and exclusion to count these leap-years. 
// Add all the years that are multiples of 4; but this includes years like 2023 that aren’t leap-years, so subtract all the years that are multiples of 100; but this excludes years like 1600 that are leap-years, so add all the years that are multiples of 400.
// Define a function daysToEndYear : int -> int that takes a year y and returns the era-day of 31/12/y. Example, daysToEndYear 1 = 365 and daysToEndYear 1792 = 654515.


let isLeap(year: int): bool = 
    if year % 400 = 0 
        then true
    elif (year % 4 = 0) && (year % 100 <> 0)
        then true
    else 
        false 

// daysToEndYear : int -> int

let getEraDays(year: int) = 

    let leapYears = List.filter isLeap [1 .. year]
    let numOfLeapDays = leapYears.Length


    (year) * 365 + numOfLeapDays

let result7 = getEraDays(1792)