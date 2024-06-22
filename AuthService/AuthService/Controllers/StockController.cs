using AutoMapper;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using AuthService.DTOs;
using AuthService.Entities;
using AuthService.Extensions;
using AuthService.Repository.Contracts;

namespace AuthService.Controllers
{
    [ApiController]
    [Route("stocks")]
    public class StockController : ControllerBase
    {
        private readonly IStockRepository _repository;

        public StockController(IStockRepository repository)
        {
            _repository = repository;
        }

        [HttpGet]
        [Authorize]
        public async Task<IActionResult> GetAll()
        {
            var roles = User.GetApiClientRoles();

            if (roles is null) return Unauthorized();

            if (roles.Contains("admin") || roles.Contains("user"))
            {
                var result = await _repository.GetAll<StockDto>();
                return result is null ? NotFound() : Ok(result);
            }
            return Forbid();
        }

        [HttpGet("{id:int}")]
        [Authorize]
        public async Task<IActionResult> GetOne(int id)
        {
            var roles = User.GetApiClientRoles();

            if (roles is null) return Unauthorized();

            // if (roles.Contains("admin"))
            // {
            //     Console.WriteLine("admin");
            //     var result = await _repository.GetById<StockDto>(id);
            //     return result is null ? NotFound() : Ok(result);
            // }

            if (roles.Contains("user"))
            {
                Console.WriteLine("user");
                var result = await _repository.GetById<StockDto>(id);
                return result is null ? NotFound() : Ok(result);
            }
            return Forbid();
        }

        [HttpPost]
        [Authorize]
        public async Task<IActionResult> Create(UpsertStockDto body, IMapper mapper)
        {
            var roles = User.GetApiClientRoles();

            if (roles is null) return Unauthorized();

            if (roles.Contains("admin") || roles.Contains("user"))
            {
                var stock = mapper.Map<Stock>(body);
                _repository.Add(stock);
                if (!await _repository.SafeChangesAsync())
                    return BadRequest("Something went wrong while posting a stock");

                var stockDto = mapper.Map<StockDto>(stock);
                return CreatedAtAction(nameof(GetOne), new { id = stock.Id }, stockDto);
            }
            return Forbid();
        }

        [HttpDelete("{id:int}")]
        [Authorize]
        public async Task<IActionResult> Delete(int id)
        {
            var roles = User.GetApiClientRoles();

            if (roles is null) return Unauthorized();

            if (!roles.Contains("admin")) return Unauthorized();

            if (roles.Contains("admin"))
            {
                var stock = await _repository.GetById(id);
                if (stock == null)
                    return NotFound();
                _repository.Delete(stock);
                if (!await _repository.SafeChangesAsync())
                    return BadRequest("Something went wrong while deleting");
                return NoContent();
            }
            return Forbid();
        }

        [HttpPut]
        public IActionResult Test()
        {
            var response = new { message = "this is a test" };
            return Ok(response);
        }
    }
}
