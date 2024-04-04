use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::hash_map::HashMap;
use std::collections::hash_set::HashSet;

const DEBUG:bool = false;

struct Tools{
    face: HashSet<String>,
    d: HashMap<String, i32>,
    s_keys: Vec<String>
}

fn main() {
    let faces: HashSet<String> = HashSet::from(["A", "K", "Q", "J", "T"].map(|x| x.to_string()));
    let mut d: HashMap<String, i32> = HashMap::from([("total", 0), ("A",0), ("K",0), ("Q",0), ("J",0), ("T",0), ("H",0), ("C",0), ("D",0), ("S",0), ("KS",0)].map(|(x, y)| (x.to_string(), y)));
    let numbers: Vec<i32> = (2..10).collect();
    let mut s_keys:Vec<String> = d.keys().map(|x| x.to_string()).collect();
    s_keys.sort();
    for x in &numbers{
        d.insert(x.to_string(), 0);
    }
    let tools = Tools{face: faces.clone(),s_keys: s_keys.clone(), d: d.clone()};


    if DEBUG{
        test(&tools);
    }
    else{
        let lines = io::stdin();
        let mut line1 = String::new();
        let mut f_half_str = String::new();
        let mut s_half_str = String::new();
        let _ = lines.read_line(&mut line1);
        let _ = lines.read_line(&mut f_half_str);
        let _ = lines.read_line(&mut s_half_str);
        let _ = trim_newline(&mut f_half_str);
        let _ = f_half_str.trim();
        let _ = trim_newline(&mut s_half_str);
        let _ = s_half_str.trim();
        let f_half: Vec<String> = f_half_str.split(" ").map(|s| s.to_string()).collect();
        let s_half: Vec<String> = s_half_str.split(" ").map(|s| s.to_string()).collect();
        
        find_res(&tools, f_half, s_half);
    }
}

fn test(tools: &Tools){
    let tests: Vec<i32> = (1..6).collect();
    for t in tests{
        if let Ok(mut lines) = read_lines(format!("input{t}.txt")) {
            let _ = lines.next();

            let f_half_str = lines.next().unwrap().expect("First half of deck input string");
            let f_half: Vec<String> = f_half_str.split(" ").map(|s| s.to_string()).collect();

            let s_half_str = lines.next().unwrap().expect("s half");
            let s_half: Vec<String> = s_half_str.split(" ").map(|s| s.to_string()).collect();
            find_res(&tools, f_half, s_half);
            
        }
    } 
}
fn find_res(tools: &Tools, fh:Vec<String>, sh:Vec<String>){
    let f_prefix = get_prefix_dict(&tools, fh.clone());
    let s_prefix = get_prefix_dict(&tools, sh.clone());
    let mut res = 0;
    for w in 1..101{
        let f_value_d = get_window_dict(tools, f_prefix.clone(), w);
        let s_value_d = get_window_dict(tools, s_prefix.clone(), w);

        for s in f_value_d.keys(){
            if s_value_d.contains_key(s){
                res = std::cmp::max(res, f_value_d[s]*2);
            }
        }
    }

    println!("{}", res);
}

// The output is wrapped in a Result to allow matching on errors.
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn get_prefix_dict(tools: &Tools, fh:Vec<String>) -> Vec<HashMap<String, i32>>{
    let mut d_prefix:Vec<HashMap<String, i32>> = vec![];
    for _ in 0..fh.len() + 1{
        d_prefix.push(tools.d.clone());
    }
    
    for i in 0..fh.len(){
        let card:String = fh[i].clone();
        let c1 = card.clone().chars().nth(0).unwrap().to_string();
        let c2 = card.clone().chars().nth(1).unwrap().to_string();
        if card == "KS".to_string(){
            *d_prefix[i+1].get_mut("KS").unwrap() = d_prefix[i+1].get("KS").unwrap() + 1;
        }

        for k in tools.d.keys(){
            *d_prefix[i+1].get_mut(k).unwrap() = d_prefix[i+1].get(k).unwrap() + d_prefix[i].get(k).unwrap();
        }

        if tools.face.contains(&c1){
            if c1 != "A".to_string(){
                *d_prefix[i+1].get_mut("total").unwrap() = d_prefix[i].get("total").unwrap() + 10;
            }
            else{
                *d_prefix[i+1].get_mut("total").unwrap() = d_prefix[i].get("total").unwrap() + 1;
            }
        }
        else{
            *d_prefix[i+1].get_mut("total").unwrap() = d_prefix[i].get("total").unwrap() + c1.parse::<i32>().unwrap();
        }
        *d_prefix[i+1].get_mut(&c1).unwrap() = d_prefix[i+1].get(&c1).unwrap() + 1;
        *d_prefix[i+1].get_mut(&c2).unwrap() = d_prefix[i+1].get(&c2).unwrap() + 1;
    }
    
    return d_prefix;
}

fn get_window_dict(tools: &Tools, d_prefix:Vec<HashMap<String, i32>>, w_size:i32)-> HashMap<String, i32>{
    let mut value_d: HashMap<String, i32> = HashMap::new();
    let mut l = 0;
    let mut r = w_size as usize;

    while r < d_prefix.len(){
        let mut dict1 = d_prefix[r].clone();
        for k in &tools.s_keys{
            *dict1.get_mut(k).unwrap() = dict1.get(k).unwrap() - d_prefix[l][k];
        }
        if dict1["KS"] == 0{
            let dict_str: &str = &tools.s_keys.iter()
                .map(|x| dict1[x].to_string())
                .collect::<Vec<_>>()
                .join(",");
            if !value_d.contains_key(dict_str){
                value_d.insert(dict_str.to_string(), dict1["total"]);
            }
        }
        l += 1;
        r += 1;
    }

    return value_d;
}
fn trim_newline(s: &mut String) {
    while s.ends_with('\n') || s.ends_with('\r') {
        s.pop();
    }
}

