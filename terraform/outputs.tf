output "application_url" {
  value = aws_lb.app_lb.dns_name
}

output "ecr_uri" {
  value = aws_ecr_repository.repo.repository_url
}