use codex_workflows_rust_service_example::normalize_event_name;

fn main() {
    let normalized = normalize_event_name("Payment Approved");
    println!("{normalized}");
}
