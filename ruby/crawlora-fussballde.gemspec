require_relative "lib/crawlora/fussballde/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-fussballde"
  spec.version = Crawlora::Fussballde::VERSION
  spec.summary = "Fussball.de API client for Crawlora (27 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted Fussball.de API. Covers amateur football clubs, players, matches, statistics, news, and federation data across 27 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=fussballde-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-fussballde", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-fussballde/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
