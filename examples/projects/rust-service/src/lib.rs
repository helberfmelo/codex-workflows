pub fn normalize_event_name(value: &str) -> String {
    value.trim().to_lowercase().replace(' ', "_")
}

#[cfg(test)]
mod tests {
    use super::normalize_event_name;

    #[test]
    fn normalizes_whitespace_and_case() {
        assert_eq!(normalize_event_name("  Order Created "), "order_created");
    }
}
